from VigenereChiper import VigenereChiper
from SteganoText import SteganoText
from Stegano import Stegano

## TEXT + IMAGE -> STEGANOIMAGE

## get files and private key if given from app
image = "../static/assets/Lenna.png"
text = "../static/assets/test.txt"
key =  "kunci"

# Instances
vc = VigenereChiper()
st = SteganoText()
stegano = Stegano()

## convert content text file to chiper and save to uploads directory
# content = vc.read(text)
# vc.encrypt(content,key)
# vc.save(text)

## convert chiper content to binary content and save to the same file
# content = st.read(text)
# st.save_to_binary(content,text)

## put binary content from text file to binary pixels of image file
# stegano.save_text_image(text,image)

## STEGANOIMAGE -> TEXT + IMAGE

# get text from image and save to originalfilename

out = stegano.expand_image(image,"inipesan")

# # # decrypt 
content = vc.read(out)
vc.decrypt(content,key)
vc.save(out)
