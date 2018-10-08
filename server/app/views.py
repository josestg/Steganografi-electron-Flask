import os
import json
from app import app
from .machine import vigenerecipher as vc
from werkzeug import secure_filename
from flask import render_template,url_for,request,flash,redirect



# UPLOADS
UPLOAD_FOLDER = "../server/app/uploads"
ALLOWED_EXTENSIONS = set(['txt','png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload',methods=['GET','POST'])
def upload():
	if request.method == 'POST':
		file = request.files['file']
		print(file.filename)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

			return redirect(url_for('upload'))
		else:
			return render_template('upload-err.html')
	else:
		return render_template('compare.html')



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

