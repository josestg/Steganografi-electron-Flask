from .SteganoImage import SteganoImage
from .SteganoText import SteganoText
import os
import numpy as np

class Stegano():

	def __init__(self):
		pass

	def save_text_image(self,textpath,imagepath):
		si = SteganoImage(imagepath)
		st = SteganoText()

		content = st.read(textpath)
		pixels = si.pixels

		if(si.numberbits < len(content)):
			print('Message so Large!')
			return None

		#save text to png
		for i in range(si.width):
			for j in range (si.height):
				(r,g,b) = pixels[i,j]
				if len(content)<3:
					if len(content)==2:
						r = content[0]
						g = content[1]
						b = b%2
					elif len(content)==1:
						r =content[0]
						g = g%2
						b = b%2
					else:
						break
				else:	
					(r,g,b) = content[:3]

				si.set_pixel((i,j),si.merge_block_lsb((r,g,b),pixels[i,j]))
				content = content[3:]
			#endfor
				
			if(len(content)<=0):
				break

		si.save(imagepath)
		os.remove(textpath)

	def expand_image(self,imagepath,outname):
		si = SteganoImage(imagepath)
		pixels = si.pixels
		header = si.header

		text = ''
		for i in range(si.width):
			for j in range(si.height):
				text+=''.join([str(e) for e in si.get_lsb(pixels[i,j])])
				header-=3
				if header<=0:
					break
			if header<=0:
				break

		if header<0:
			text=text[:header]

		ext = text[si.headersize : si.headersize+si.extsize]
		content = text[si.headersize + si.extsize :]

		ext = ''.join([ chr(int(ext[i:i+8],2)) for i in range(0,24,8) ])

		st = SteganoText()
		basepath = imagepath.split('/')[:-1]
		basepath = '/'.join(basepath)
		textpath = basepath+'/'+outname+'.'+ext
		st.binary_to_content(content)
		st.save(textpath)
		return textpath

#end