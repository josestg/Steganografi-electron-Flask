from .VigenereChiper import VigenereChiper
from .SteganoText import SteganoText
from .Stegano import Stegano
import os

## TEXT + IMAGE -> STEGANOIMAGE
def put_txt_to_img(data):
	text = os.path.join(data['basepath'],data['txtname'])
	img  = os.path.join(data['basepath'],data['imgname'])

	key = data['key']
	
	#Vigenere Process
	vc = VigenereChiper()
	content = vc.read(text)
	vc.encrypt(content,key)
	vc.save(text)

	## convert content to binary and save to the same file
	st = SteganoText()
	content = st.read(text)
	st.save_to_binary(content,text)

	## put binary content from text file to binary pixels of image file
	stegano = Stegano()
	stegano.save_text_image(text,img)

## STEGANOIMAGE -> TEXT + IMAGE 
def get_txt_from_img(data):
	key = data['key']
	text = os.path.join(data['basepath'],data['txtname'])
	img  = os.path.join(data['basepath'],data['imgname'])

	stegano = Stegano()
	vc = VigenereChiper()
	stegano.expand_image(img,text)

	# # decrypt 
	content = vc.read(text)
	vc.decrypt(content,key)
	vc.save(text)