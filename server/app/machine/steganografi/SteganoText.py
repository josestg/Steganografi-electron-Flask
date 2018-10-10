class SteganoText():

	def __init__(self):
		print('STEGANO TEXT')
		self.headersize = 32
	
	def read(self,path):
		self.__file = open(path,'r')
		self.__content = self.__file.read()
		self.__file.close()
		return self.__content

	def set_content(self,content):
		self.__content = content
	def get_content(self):
		return self.__content

	def save(self,path):
		file = open(path,'w')
		file.write(self.__content)
		file.close()

	def get_binary_tape(self,content):
		binarytape = ''
		for c in content:
			binarytape+='{0:08b}'.format(int(ord(c)))
		return binarytape

	def set_header(self,bintape):
		header = '{0:032b}'.format( int(len(bintape))+self.headersize) 
		fullcontent = header + bintape
		self.__content = fullcontent

	def save_to_binary(self,content,path):
		bintape = self.get_binary_tape(content)
		self.set_header(bintape)
		self.save(path)

	def binary_to_content(self,bintape):
		content=''
		while len(bintape)>0:
			char = bintape[:8]
			bintape = bintape[8:]
			content+=chr(int(char,2))
		self.__content = content
		return self.__content

	def expand_fullcontent(self):
		fullcontent = self.__content
		header = fullcontent[0:self.headersize]
		content = fullcontent[self.headersize:]
		header = int(header,2)
		return header,content



def main():
	st = SteganoText()
	content = st.read("../../uploads/pesan.txt")
	# header,content = st.expand_fullcontent()
	# st.binary_to_content(content)
	# st.save('../../uploads/pesan.txt')
	# # print('header : ',header)
	# # print('content : ',content)
	st.save_to_binary(content,"../../uploads/pesan.txt")

if __name__ == '__main__':
	main()
