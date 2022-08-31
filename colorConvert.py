import colorsys

from main import Image, ImageOps, save_image

def image_gray_scale(img):
    new_img = ImageOps.grayscale(img)

    return new_img

def image_rgb_2_hsv(img):
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

        print(len(Hdat))
    
        hsv_image = Image.merge('RGB', (r, g, b))

        save_image(hsv_image)

        return hsv_image


'''
new_op_img = Image.open("imgs\img_bmp_16.bmp")
img_to_save = image_rgb_2_hsv(new_op_img)
img_to_save.show()
'''
