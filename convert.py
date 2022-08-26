import colorsys
from PIL import Image, ImageOps

def imageGrayScale(imgtToConvert):
    newImg = ImageOps.grayscale(imgtToConvert)

    return newImg

def rgbToHSV(img):
        r, g, b = img.split()
        Hdat = []
        Sdat = []
        Vdat = []

        for rd, gn, bl in zip(r.getdata(), g.getdata(), b.getdata()):
            h, s, v = colorsys.rgb_to_hsv(rd / 255., gn / 255., bl / 255.)
            Hdat.append(int(h * 255.))
            Sdat.append(int(s * 255.))
            Vdat.append(int(v * 255.))

        r.putdata(Hdat)
        g.putdata(Sdat)
        b.putdata(Vdat)

        print('H = {} \n S = {} \n V = {}'.format(Hdat, Sdat, Vdat))

        return Image.merge('RGB', (r, g, b))

a = Image.open("img_bmp_16.bmp")
b = rgbToHSV(a)
b.save("convertida.jpg")
b.show()


