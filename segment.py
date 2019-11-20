import numpy as np
import imageio
import char_reg
from scipy import ndimage
def image_processing(image_name):
	image = imageio.imread(image_name)
	# Convert to grayscale
	image = image.mean(axis = 2)
	# Convert to binary
	image[image >  128] = 255
	image[image <= 128] = 0
	# Convert to zeros and ones
	image[image == 255] = 1
	# Invert the image
	image = 1 - image
	# Create the structuring element
	structuring_element = np.ones((1, 5))
	# Perform dilation
	eroded_image = ndimage.binary_dilation(image, structure=structuring_element).astype(np.uint8)
	#imageio.imwrite('eroded_image.jpg', eroded_image.astype(np.uint8) * 255)
	
	def generate_tuples(mask, threshold=10):
		mask[mask < threshold] = 0
		mask[mask >= threshold] = 1
		mask1 = np.concatenate(([0], mask))
		mask2 = np.concatenate((mask, [0]))
		mask = np.logical_xor(mask1, mask2).astype(np.uint8)
		indices = [index for (index, value) in enumerate(mask) if value == 1]
		return list(zip(indices[::2], indices[1::2]))
	tuples = generate_tuples(eroded_image.sum(axis=1))
	line = ''
	strg= ' '
	for (begin, end) in tuples:
		sub_image = image[begin:end, :]
		#imageio.imwrite('horizontal/image_' + str(begin) + '.jpg', sub_image)
		line = '$'
		vertical_tuples = generate_tuples(sub_image.sum(axis=0), threshold=3)
		for (begin_col, end_col) in vertical_tuples:
			sub_sub_image = sub_image[:, begin_col:end_col]
			imageio.imwrite('vertical/image_' + str(begin) + str(begin_col) + '.jpg', sub_sub_image)
			s=char_reg.predict('vertical/image_' + str(begin) + str(begin_col) + '.jpg')
			line += s
		line+='$'
		line+= '\n'
		strg +=line
	return(strg)
		
 		
		



