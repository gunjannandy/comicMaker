from PIL import Image

#converts RGBA images to RGB

def imageConverter(filename):
		im = Image.open(filename)
		rgb_im = im.convert('RGB')
		rgb_im.save(filename)