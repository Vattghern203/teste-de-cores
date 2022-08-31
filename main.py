from colorsys import rgb_to_hsv
from PIL import Image, ImageOps

# from convert import image_gray_scale, image_rgb_2_hsv
from defaultFunctions import save_image

'''img = Image.open(r"../imgs/photo_1.webp")
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

img_jaco = Image.open(r"imgs/jaco.jpg")
img_jaco_hsv = image_rgb_2_hsv(img_jaco)
save_image(img_jaco_hsv, "jaco_bolado")
img_jaco_hsv.show()'''

img = Image.open(r"imgs/original/cafe_base.png").convert('RGB')
img_scan = Image.open(r"imgs/original/cafe.jpg").convert('RGB')

img_data = list(img.getdata())

print(img_data[0][1])

range = img.getextrema()

print(range)

red_range_min = range[0][0]
red_range_max = range[0][1]

print(img.width, img.height)

ok = []

img_scan_pixels = list(img_scan.getdata())

for pixel in img_scan_pixels:
    if pixel >= (87, 1, 0) and pixel <= (255, 171, 248):
        img_scan.putpixel()
        print("OK")

        ok.append(pixel)

    else:

        print("No")

print(ok)
img_scan.show()


    
    





