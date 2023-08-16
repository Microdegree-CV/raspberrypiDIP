from PIL import Image
im = Image.open("../dataset/misc/4.1.07.tiff")
print(im.mode)
print(im.format)
print(im.size)
print(im.info)
print(im.getbands())
