from flask import Flask, render_template, request
from werkzeug import secure_filename
import pdf2image
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		f = request.files['myFile']
		f.save(secure_filename(f.filename))
		name=f.filename
		resul=pdf2image.p2f(name)
		return render_template('index.html',value=resul)
		
if __name__ == '__main__':
   app.run(debug = True)
