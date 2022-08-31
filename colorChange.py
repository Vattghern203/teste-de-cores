from PIL import Image

img = Image.open(r"imgs/original/cafe.jpg").convert('RGB')
img_reference = Image.open(r"imgs/original/cafe_base.png").convert('RGB')

pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if pixels[i, j] >= (87, 1, 0) and pixels[i, j] <= (255, 171, 248):
            img.putpixel((i, j), (0, 100, 255))

img.show()