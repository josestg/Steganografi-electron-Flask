
import sys

def unicode_table():
	for i in range(0,256):
		for j in range(0,256):
			print(chr(((i+j)%256)),end=' ')
		print('')

def encrypt_text(plain,key):
	i = 0
	ch = ''
	for p  in plain:
		ch += chr((ord(p)+ord(key[i%len(key)]))%265)
		i+=1
	return ch

def decrypt_text(ch,key):
	i = 0
	plain = ''
	for c  in ch:
		plain += chr(abs((ord(c)-ord(key[i%len(key)]))%265))
		i+=1
	return plain

def save_file(ch,name):
	file = open(name,'w+')
	file.write(ch)
	file.close()
	
def read_file(file):
	file = open(file,'r')
	content = file.read()
	file.close()
	return content


if __name__ == "__main__":
	main()
	