import ImageStegano as IS
import TextStegano as TS
import math

class Steganografi():
	def __init__(self,image,text,key=None):
		self.__image = IS.ImageStegano(image)
		self.__text = TS.TextStegano(text)


	def add(self,X,x):
		if X%2!=x:
			if x==1:
				return X+1
			else:
				return X-1
		return X

	def add_head(self):
		binary_text = self.__text.to_binary()
		head = '{0:032b}'.format( int(len(binary_text))) 
		full_text ='{0:032b}'.format( int(len(binary_text)))+binary_text
		return full_text

	def hide_text_to_image(self):

		full_text = self.add_head()

		if self.__image.num_lsb() >= len(full_text):
			# Imange can contains all bit of message in LSB
			i = 0
			j = 0
			pixels = self.__image.get_pixels()

			while len(full_text) > 0 and i< self.__image.height:
				R,G,B = pixels[i,j]
				print(pixels[i,j],end=" -> ")

				if len(full_text)<3:
					# no blue value
					if len(full_text) ==1:
						r = rgb[0]
						(R,G,B) = (self.add(R,int(r)),G,B)
						print(r,end=" -> ")
					else:
						r = rgb[0]
						g = rgb[1]
						(R,G,B) = (self.add(R,int(r)),self.add(G,int(g)),B)
						print(r,g,end=" -> ")
				else:
					#red blue and red exsist
					rgb = full_text[:3]
					r,g,b = rgb
					(R,G,B) = (self.add(R,int(r)),
								self.add(G,int(g)),
									self.add(B,int(b))
								)
					print(r,g,b,end=" -> ")


				full_text = full_text[3:]

				self.__image.set_pixel((i,j),(R,G,B))
				print(pixels[i,j])
				j+=1
				if j==self.__image.width-1:
					j=0
					i+=1	
			#endwhile
			self.__image.save_image(self.__image.info["path"])

	def extract_image(self):
		length = ''
		pixels = self.__image.get_pixels()
		# print(pixels[0,0])
		i = 0
		while len(length)<33:
			length+=''.join(str(e) for e in self.__image.get_lsb(pixels[0,i]) )
			i+=1
		length = int(length[0:32],2)
		string_binary =''
		size = math.ceil(length/3)*3

		print(size)
		for j in range(0,self.__image.height):
			for k in range(0,self.__image.width):
				if len(string_binary) < size:
					string_binary+=''.join(str(e) for e in self.__image.get_lsb(pixels[j,k]))
				else:
					break
		string_binary = string_binary[32:length]
		print(string_binary)
		self.__image.save_image('../uploads/ex.png')
		self.__text.save_file(string_binary,'../uploads/ex.txt')

	


stegano  = Steganografi('../uploads/test.png','../uploads/pesan.txt')
# print(stegano.add_head()[0:32])
# stegano.add_head()
# stegano.extract_image()
# stegano.get_bits_lsb()
# stegano.hide_text_to_image()
