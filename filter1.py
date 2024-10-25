from PIL import Image, ImageFilter 

i = Image.open('Image.JPG')
blur = i.filter(ImageFilter.BoxBlur(10))
blur.save('blur.png')

edge = i.filter(ImageFilter.FIND_EDGES)
edge.save('edge.png')