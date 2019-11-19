from wand.image import Image as wi
import segment 
def p2f(name):
	pdf = wi(filename=name, resolution=300)
	pdfimage = pdf.convert("png")
	i=1
	#convert to image
	for img in pdfimage.sequence:
		page = wi(image=img)
		page.save(filename=str(i)+".png")
		s=segment.image_processing(str(i)+".png")
		return(s)
	
