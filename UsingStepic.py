# import image
from PIL  import Image
import stepic

i = Image.open('test.jpg')

i.show()

# Could open a file here
# f = open('myfile','r')
# text = f.read()

steg = stepic.encode(i,'This is some text')
# steg = stepic.encode(i,text)

steg.save('steg.jpg','JPEG')
i2 = Image.open('steg.jpg')
i2.show()
