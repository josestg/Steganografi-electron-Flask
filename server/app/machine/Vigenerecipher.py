
class VigenereChiper():

	def __init__(self,path):
		self.__path = path
		self.__info = {'filename':path}

	def read_file(self):
		file = open(self.__path,'r')
		self.__content = file.read()
		file.close()

	def get_content(self):
		self.read_file()
		return self.__content

	def encrypt_text(self,key):
		content = self.get_content()
		self.__content = ''
		i = 0
		for c  in content:
			self.__content += chr((ord(c)+ord(key[i%len(key)]))%265)
			i+=1
		self.save_file()
		return self.__content
		
	def decrypt_text(self,key):
		content = self.get_content()
		self.__content = ''
		i = 0
		for c  in content:
			self.__content += chr(abs((ord(c)-ord(key[i%len(key)]))%265))
			i+=1
		self.save_file()
		return self.__content

	def save_file(self):
		file = open(self.__path,'w+')
		file.write(self.__content)
		file.close()

	def unicode_table(self,x=65,y=91):
		n = y-x
		table = list()
		column = list()
		for i in range(0,n):
			for j in range(0,n):
				column.append(chr((x+((i+j)%(y-x)))))
			table.append(column)
			column = []
		return table
