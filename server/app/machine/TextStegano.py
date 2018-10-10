
class TextStegano():
	def __init__(self,path):
		self.__path = path

	def read_file(self):
		file = open(self.__path,'r')
		self.__content = file.read()
		file.close()
		return self.__content

	def save_file(self,path):
		file = open(path,'w')
		file.write(self.__content)
		file.close()		

	def get_binary_string(self,content):
		bin_str = ''
		for c in content:
			bin_str+='{0:08b}'.format( int(ord(c)))
		return bin_str

	def get_content(self):
		return self.__content
	def set_content(self,content):
		self.__content = content
		self.save_file(self.__path)

	def set_header_content(self,bin_str):
		header = '{0:032b}'.format( int(len(bin_str))) 
		self.__content = header + bin_str
		self.save_file(self.__path)

	def binary_to_text(self,bin_str):
		head = 0
		tail = 8
		header = bin_str[0:32]
		print(header)
		content = bin_str[32:]
		self.__content = ''
		while tail <= len(content):
			self.__content += chr(int(content[head:tail],2))
			head+=8
			tail+=8
		return self.__content

#END

def main():
	ts = TextStegano("../uploads/pesan.txt")
	content = ts.read_file()
	# bin_str = ts.get_binary_string(content)
	# ts.set_header_content(bin_str)
	text = ts.binary_to_text(content)
	ts.set_content(text)


if __name__ == "__main__":
	main()