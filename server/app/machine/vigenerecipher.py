def unicode_table(x,y):
	n = y-x
	table = list()
	column = list()
	for i in range(0,n):
		for j in range(0,n):
			column.append(chr((x+((i+j)%(y-x)))))
		table.append(column)
		column = []
	return table

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

def save_file(ch,target):
	file = open(target,'w+')
	file.write(ch)
	file.close()
	
def read_file(file):
	file = open(file,'r')
	content = file.read()
	file.close()
	return content

def main():
	unicode_table(65,70)

if __name__ == "__main__":
	main()
	