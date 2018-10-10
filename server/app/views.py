import os
import json
from app import app
from .machine import vigenerecipher as vc
from werkzeug import secure_filename
from flask import render_template,url_for,request,redirect
from .machine import steganografi as sg


# GLOBAL VARIABLES
UPLOAD_FOLDER = "../server/app/uploads"
ALLOWED_TEXT_EXTENSIONS  = 	set(['txt','dat'])
ALLOWED_IMAGE_EXTENSIONS =	set(['png', 'bmp', 'jpg'])
ERRORS_LOG = []
PRIVATE_KEY = None

# UPLOADS 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename,rules):
	return '.' in filename and filename.rsplit('.',1)[1] in rules


@app.route('/upload',methods=['GET','POST'])
def upload():
	if request.method == 'POST':
		global ERRORS_LOG
		ERRORS_LOG = []
		imagefile = request.files['image']
		textfile = request.files['massage']

		#with private key
		if request.form.getlist('reqpassword'):
			global PRIVATE_KEY 
			PRIVATE_KEY = request.form['password']
		if imagefile and textfile:
			if allowed_file(imagefile.filename,ALLOWED_IMAGE_EXTENSIONS):
				imagename = secure_filename(imagefile.filename)
				# imagefile.save(os.path.join(app.config['UPLOAD_FOLDER'],imagename))
			else:
				Log = "Extention Error : Allowed image extention => ({})".format(ALLOWED_IMAGE_EXTENSIONS)
				ERRORS_LOG.append(Log)

			if allowed_file(textfile.filename,ALLOWED_TEXT_EXTENSIONS):
				textname = secure_filename(textfile.filename)
				# textfile.save(os.path.join(app.config['UPLOAD_FOLDER'],textname))
				decrypt(os.path.join(app.config['UPLOAD_FOLDER'],textname),'THIS KEY')
			else:
				Log = "Extention Error : Allowed text extention => ({})".format(ALLOWED_TEXT_EXTENSIONS)
				ERRORS_LOG.append(Log)
		else:
			ERRORS_LOG.append('Directory Error : File Not Found')

		if ERRORS_LOG : # ERROR EXIST
			return redirect(url_for('error'))
		else:
			return redirect(url_for('success'))
	else:
		return redirect(url_for('upload'))

#END UPLOAD

#VIGENERE
def encrypt(file,key):
	content = vc.read_file(file)
	chiper  = vc.encrypt_text(content,key)
	vc.save_file(chiper,file)
	return chiper

def decrypt(file,key):
	content = vc.read_file(file)
	plain = vc.decrypt_text(content,key)
	vc.save_file(plain,file)
	return plain	
#END VIGENERE

#LSB

#END LSB


@app.route('/')
def index():
	return redirect(url_for('about'))
    # return render_template("index.html",path=os.path.join(app.config['UPLOAD_FOLDER'],'pesan.txt'))

@app.route('/success')
def success():
	if PRIVATE_KEY is not None:
		return render_template('compare.html',key=PRIVATE_KEY)
	else:
		return render_template('compare.html',key=ERRORS_LOG)

@app.route('/error')
def error():
	return render_template('index.html',ERRORS_LOG=ERRORS_LOG)

@app.route('/about')
def about():
	pixels = sg.get_pixels(os.path.join(app.config['UPLOAD_FOLDER'],'test.png'))
	return render_template("about.html",pixels=pixels)