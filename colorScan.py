from main import Image, ImageOps, save_image, rgb_to_hsv

img_to_scan = Image.open(r"imgs/samples/coffee_original.jpg").convert('RGB')
img_sample = Image.open(r"imgs/samples/coffee_sample.png").convert('RGB')

pixels = img_to_scan.load()

for i in range(img_to_scan.size[0]):
    for j in range(img_to_scan.size[1]):
        if pixels[i, j] >= (87, 1, 0) and pixels[i, j] <= (255, 171, 248):
            img_to_scan.putpixel((i, j), (0, 100, 255))

img_to_scan.show()
