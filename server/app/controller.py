import os
from werkzeug import secure_filename

def allowed_file(filename,rules):
	return '.' in filename and\
		 filename.rsplit('.',1)[1] in rules

def upload(req,dest):
	IMG_EXT = set(['png', 'bmp', 'jpg'])
	TXT_EXT = set(['txt','dat'])
	data = {
		'basepath':dest,
		'imgname' : 'noimage.png',
		'key':'kunci',
	}
	errors = set()

	imgfile = req.files["image"]
	txtfile = req.files["massage"]

	#private key
	if req.form.getlist("reqpassword"):
		key = req.form["password"]

	if imgfile and txtfile:
		if allowed_file(imgfile.filename,IMG_EXT):
			imgname = secure_filename(imgfile.filename)
			data['imgname'] =imgname
			imgfile.save(os.path.join(dest,imgname))
		else:
			error = "Extention Error : \
					Allowed image extention \
						=> ({})".format(IMG_EXT)
			errors.add(error)
		if allowed_file(txtfile.filename,TXT_EXT):
			txtname = secure_filename(txtfile.filename)
			data['txtname'] =txtname
			txtfile.save(os.path.join(dest,txtname))
		else:
			error = "Extention Error : \
					Allowed Text extention \
						=> ({})".format(TXT_EXT)
			errors.add(error)
	else:
		errors.add('Directory Error : \
					 File Not Found')

	data['errors'] = errors

	return data

