from flask import Flask, render_template, request
import pdf2image
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.files.get('myFile')
		nme=result.filename
		resul=pdf2image.p2f(nme)
		return render_template('index.html',value=resul)
		#return ' %s  ' % (nme)


if __name__ == '__main__':
   app.run(debug = True)
