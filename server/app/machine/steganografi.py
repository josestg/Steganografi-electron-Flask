from . import ImageStegano
from . import TextStegano

class Stegano():
	def __init__(self,image,text,key=None):
		self.__image = ImageStegano(image)
		self.__text = TextStegano(text)
