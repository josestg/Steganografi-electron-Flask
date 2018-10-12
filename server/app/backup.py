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
				imagefile.save(os.path.join(app.config['UPLOAD_FOLDER'],imagename))
				DATA['image']=imagename
				DATA['default'] =imagename
			else:
				Log = "Extention Error : Allowed image extention\
						 => ({})".format(ALLOWED_IMAGE_EXTENSIONS)
				ERRORS_LOG.append(Log)

			if allowed_file(textfile.filename,ALLOWED_TEXT_EXTENSIONS):
				textname = secure_filename(textfile.filename)
				textfile.save(os.path.join(app.config['UPLOAD_FOLDER'],textname))
				DATA['text']=textname
				DATA['key']=PRIVATE_KEY

				addr =ps.run(DATA)
				return render_template('compare.html',data=DATA)

			else:
				Log = "Extention Error : Allowed text extention\
						 => ({})".format(ALLOWED_TEXT_EXTENSIONS)
				ERRORS_LOG.append(Log)
		else:
			ERRORS_LOG.append('Directory Error : File Not Found')