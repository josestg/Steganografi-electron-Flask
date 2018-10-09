class TextStegano():
	def __init__(self,file):
		self.__file = open(file,'r')
		self.__content = self.__file.read()
		self.__file.close()
		self.__info = {'filename':self.__file.name}

	def to_binary(self):
		self.__bin_str = ''
		for c in self.__content:
			self.__bin_str+='{0:08b}'.format( int(ord(c)))
		return self.__bin_str

	def binary_to_text(self,bin_str):
		head = 0
		tail = 8
		self.__text = ''
		while tail <= len(bin_str):
			self.__text += chr(int(bin_str[head:tail],2))
			head+=8
			tail+=8
		return self.__text

	def get_info(self):
		return self.__info
