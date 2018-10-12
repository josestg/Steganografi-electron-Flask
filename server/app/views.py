import json
from app import app,controller
from flask import render_template,url_for,request,redirect
from .machine import main

app.config['UPLOAD_FOLDER'] = "../server/app/static/assets"
args = {}

@app.route('/upload_file',methods=['GET','POST'])
def upload_file():
	if request.method == 'POST':
		data = controller.upload(request,app.config['UPLOAD_FOLDER'])
		if data['errors'] : # ERROR EXIST
			return redirect(url_for('error'))
		else:
			main.put_txt_to_img(data)
			args ['imgname'] = data['basepath'] + data['imgname']
			return redirect(url_for('success'))
	else:
		return redirect(url_for('upload'))


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/success')
def success():
	return render_template('compare.html',data=args)

@app.route('/error')
def error():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template("about.html")