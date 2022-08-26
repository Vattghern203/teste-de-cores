from colorsys import rgb_to_hsv
from PIL import Image, ImageOps

img = Image.open(r"../imgs/photo_1.webp")
img2 = Image.open(r"../imgs/img_bmp_16.bmp")
imgTree = Image.open(r"../imgs/tree7.jpg")
imgPSD = Image.open(r"../imgs/ImagemOriginal.psd")

img3 = ImageOps.grayscale(imgPSD)

img3.show()

imgToSave = img.save("savedPhoto.jpg")

r, g, b = imgPSD.split()
len(r.histogram())

histogramR = r.histogram(mask=None, extrema=None)
histogramG = g.histogram()
histogramB = b.histogram()

print('R = {} \n\n G = {} \n\n B = {}'.format(histogramR, histogramG, histogramB))

print(img.histogram())





