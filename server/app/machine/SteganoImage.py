import numpy as np 
import math
from PIL import Image

class SteganoImage():
	def __init__(self,path):
		try:
			self.__path = path
			self.__im 	= Image.open(self.__path)
			self.__pixels = self.__im.load()
			self.width,self.height = self.__im.size
			self.headersize = 32
		except FileNotFoundError as e:
			raise e

	@property
	def path(self):
		return self.__path
	@property
	def image(self):
		return self.__im
	@property
	def pixels(self):
		return self.__pixels
	@property
	def numberbits(self):
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
		try:
			self.__im.save(path)
		except FileNotFoundError as e:
			raise e
			
	@property
	def header(self):
		header = ''
		n = math.ceil(self.headersize/3)
		for i in range(n):
			header+=''.join([str(e) for e in self.get_lsb(self.__pixels[0,i])])
		return int(header[:self.headersize],2)

