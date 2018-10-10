import os
from steganografi import SteganoText,SteganoImage

class Stegano():

	def __init__(self):
		pass

	def save_text_image(self,textpath,imagepath):
		si = SteganoImage(imagepath)
		st = SteganoText()

		content = st.read(textpath)
		pixels = si.get_pixels()

		if(si.get_nums_bit() < len(content)):
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

	def expand_image(self,imagepath,textpath):
		si = SteganoImage(imagepath)
		pixels = si.get_pixels()
		header = si.get_header()

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
		content = text[si.headersize:]

		st = SteganoText()
		st.binary_to_content(content)
		st.save(textpath)

def main():
	stegano = Stegano()
	# stegano.save_text_image("../../uploads/pesan.txt","../../uploads/Lenna.png")
	# stegano.expand_image("../../uploads/Lenna.png","../../uploads/pesan.txt")

if __name__ == "__main__":
	main()

