import numpy as np
from PIL import Image


class ImageStegano():

	def __init__(self,file):
		self.__img = Image.open(file)
		self.__pixels = self.__img.load()
		self.width = self.__img.width
		self.height = self.__img.height

	def get_pixels(self):
		return self.__pixels

	def pixel_to_binary(self,RGB):
		R,G,B = RGB
		return ( '{0:08b}'.format( int(R)) ,
					'{0:08b}'.format( int(G)),
					  '{0:08b}'.format( int(B)))


	def set_pixel(self,xy,rgb):
		x,y = xy
		self.__pixels[x,y] = rgb

	def get_pixel_lsb(self,rgb):
		(R,G,B) = map(lambda x: x%2 ,rgb)
		return (R,G,B)

	def num_lsb(self):
		return self.__img.height*self.__img.width*3

	def save_image(self,path):
		self.__img.save(path)


def main():
	str_bin=''	
	ist = ImageStegano("../uploads/test.png")
	pixels = ist.get_pixels()
	for i in range(0,ist.height):
		for j in range(0,ist.width):
			str_bin+=''.join(str(e) for e in ist.get_pixel_lsb(pixels[0,i]) )

	print(str_bin)
if __name__ == "__main__":
	main()
