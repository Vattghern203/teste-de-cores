from email.mime import image
from PIL import Image, ImageOps

img = Image.open("photo_1.webp")
img2 = Image.open(r"img_bmp_16.bmp")
imgTree = Image.open(r"tree7.jpg")
imgPSD = Image.open(r"ImagemOriginal.psd")

def imageMatrix(imgToConvert):
    cores = []
    for cor in imgToConvert.getdata():
        if cor not in cores:
            cores.append(cor)

    return print(cores)

def imageGrayScale(imgtToConvert):
    newImg = ImageOps.grayscale(imgtToConvert)

    return newImg

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





