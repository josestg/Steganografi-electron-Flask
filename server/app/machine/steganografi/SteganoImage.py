

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


def save_text_png():
	si = SteganoImage("../../uploads/Lenna.png")
	st = ST.SteganoText()
	content = st.read("../../uploads/pesan.txt")
	pixels = si.get_pixels()
	#save text to png
	for i in range(si.width):
		for j in range (si.height):
			(r,g,b) = pixels[i,j]
			if len(content)<3:
				if len(content)==2:
					r = content[0]
					g = content[1]
					r = r%2
				elif len(content)==1:
					r =content[0]
					g = g%2
					b = b%2
				else:
					break
			else:	
				(r,g,b) = content[:3]
			print(pixels[i,j],' -> (',r,g,b,')',end=" -> ")
			si.set_pixel((i,j),si.merge_block_lsb((r,g,b),pixels[i,j]))
			print(pixels[i,j])
			content = content[3:]
		if(len(content)<=0):
			break
	si.save('../../uploads/Lennacopy.png')

def expand_image():
	si = SteganoImage("../../uploads/Lennacopy.png")
	pixels = si.get_pixels()
	header = si.get_header()
	length = header
	endl = 0
	text = ''
	for i in range(si.width):
		for j in range(si.height):
			text+=''.join([str(e) for e in si.get_lsb(pixels[i,j])])
			length-=3
			if length<=0:
				break
		if length<=0:
			break
	if length<0:
		text=text[:length]
	content = text[si.headersize:]

	st = ST.SteganoText()
	realtext = st.binary_to_content(content)
	st.save('../../uploads/pesan2.txt')
	# print(realtext)

def main():
	# save_text_png()
	expand_image()


if __name__ == "__main__":
	main()