from flask import Flask, request, render_template, redirect, url_for, Response
from werkzeug import secure_filename
from utils import build_file_name
import os
from config import app
from models import Igualito
from google.appengine.ext.webapp.util import run_wsgi_app

@app.context_processor
def insertar_ultimos():
	ultimos = Igualito.all()
	return dict(ultimos=ultimos)

@app.route("/")
def index():
	igualitos = Igualito.all()
	return render_template('index.html', igualitos=igualitos )

@app.route("/upload/", methods=['POST', 'GET'])
def upload():
	if request.method == 'POST':
		file1 = request.files['pic1']
		file2 = request.files['pic2']
		filename1 = build_file_name(file1.filename)
		filename2 = build_file_name(file2.filename)
	
		
		data = Igualito()
		data.nombre = request.form['name']
		data.imagen1 = file1.read()
		data.imagen2 = file2.read()
		data.put()
		
		return redirect(url_for('uploaded_end', file1=None, file2=None	))
		
	return render_template('upload.html')
	
@app.route('/upload_end')
def uploaded_end():
	return render_template('uploaded_file.html')
	
@app.route('/imagen1/<key>')
def uploaded_file(key):
	igualito = Igualito.get(key)
	return Response(igualito.imagen1, mimetype='image/jpeg')

@app.route('/imagen2/<key>')
def uploaded_file(key):
	igualito = Igualito.get(key)
	return Response(igualito.imagen2, mimetype='image/jpeg')
 
	
@app.route('/show/')
@app.route("/show/<name>")
def post(name=None):
	return render_template('index.html', name=name)
	
@app.route("/get", methods=['POST'])
def obtener():
	pass

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
	

def main():
	run_wsgi_app(app)
	
if __name__ == "__main__":
	main()