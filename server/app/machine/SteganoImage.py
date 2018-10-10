import numpy as np 
import math
from PIL import Image

class SteganoImage():
	def __init__(self,path):
		print('STEGANO IMAGE')
		self.__path = path
		self.__im 	= Image.open(self.__path)
		self.__pixels = self.__im.load()
		self.width,self.height = self.__im.size
		self.headersize = 32

	def get_path(self):
		return self.__path

	def get_image(self):
		return self.__im

	def get_pixels(self):
		return self.__pixels

	def get_nums_bit(self):
		return 3*self.width*self.height

	def set_pixel(self,xy,rgb):
		(R,G,B) = rgb
		x,y = xy
		self.__pixels[x,y] = (R,G,B)

	def get_lsb(self,pixels):
		(r,g,b) = map(lambda e: e%2,pixels)
		return (r,g,b)

	def switch(self,X,x):
		if X%2!=int(x):
			if int(x)==1:
				return X+1
			else:
				return X-1
		return X

	def merge_block_lsb(self,block,pixels):
		(r,g,b) = map(self.switch , pixels,block)
		return (r,g,b)

	def save(self,path):
		self.__im.save(path)

	def get_header(self):
		header = ''
		n = math.ceil(self.headersize/3)
		for i in range(n):
			header+=''.join([str(e) for e in self.get_lsb(self.__pixels[0,i])])
		return int(header[:self.headersize],2)


def main():
	pass


if __name__ == "__main__":
	main()