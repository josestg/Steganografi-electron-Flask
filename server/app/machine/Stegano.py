import ImageStegano as IS
import TextStegano as TS
import math

class Stegano():

	def __init__(self):
		pass

	def switch(self,X,x):
		if X%2!=x:
			if x==1:
				return X+1
			else:
				X-1
		return X

	def hide_text_to_image(self,textfile,imagefile):
		
		ts = TS.TextStegano(textfile)
		textcontent = ts.read_file()
		bin_str = ts.get_binary_string(textcontent)
		ts.set_header_content(bin_str)
		
		# full_str = header + content
		full_str = ts.read_file()

		ist = IS.ImageStegano(imagefile)
		pixels = ist.get_pixels()

		if ist.num_lsb() >= len (full_str):
			# Imange can contains all bit of message in LSB
			i,j = (0,0)
			while len(full_str)>0 and i < ist.height:
				R,G,B =  pixels[i,j]
				rgb = full_str

				print(pixels[i,j],end="->")
				if len(full_str)<3:
					if len(full_str)==2:
						r = rgb[0]
						b =	rgb[1]
						(R,G,B) = (self.switch(R,int(r)),
									self.switch(G,int(g)),
									  B)
						print(r,g,end=' -> ')
					else:
						r = rgb[0]
						(R,G,B) = (self.switch(R,int(r)),G,B)
						print(r,end=' -> ')
				else:
					rgb = full_str[:3]
					r,g,b = rgb
					(R,G,B) = (self.switch(R,int(r)),
								self.switch(G,int(g)),
								  self.switch(B,int(b))
								)
					print(r,g,b,end=' -> ')

				full_str = full_str[3:]
				ist.set_pixel((i,j),(R,G,B))
				print(pixels[i,j])
				j+=1

				if j>= ist.width :
					j = 0
					i+=1
			ist.save_image("../uploads/ex.png")
			#endwhile
		else:
			#Image can't contains message
			pass


	def extract_text_from_image(self,imagefile):
		ist = IS.ImageStegano(imagefile)
		pixels = ist.get_pixels()
		header = ''
		i,j = (0,0)
		while True and i< ist.height:
			header+=''.join(str(e) for e in ist.get_pixel_lsb(pixels[i,j]))
			j+=1
			if len(header) >= 32:
				break
			if j>= ist.width:
				i+=1
				j =0
		header = header[:32]
		length = int(header,2)
		print(length)

def main():
	st = Stegano()
	# st.hide_text_to_image('../uploads/pesan.txt','../uploads/Lenna.png')
	st.extract_text_from_image('../uploads/ex.png')


if __name__ == "__main__":
	main()