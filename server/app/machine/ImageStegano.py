import numpy as np
from PIL import Image

class ImageStegano():

	def __init__(self,file):
		self.__img = Image.open(file)
		self.__info = {}

	def get_lsb(self,rgb):
		(R,G,B) = map(lambda x: x%2 ,rgb)
		return (R,G,B)

	def get_pixels(self):
		return self.__img.load()

	def num_lsb(self):
		return self.__img.height*self.__img.width*3

	def get_info(self):
		self.__info['file']= self.__img.filename
		return self.__info