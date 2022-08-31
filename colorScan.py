from main import Image, ImageOps, save_image, rgb_to_hsv
import time

img_to_scan = Image.open(r"imgs/samples/coffee_original.jpg").convert('RGB')
img_sample = Image.open(r"imgs/samples/coffee_sample.png").convert('RGB')

range_color = img_sample.getextrema()

print("Máximos e mínimos dos valores RGB da amostra de cor:", range_color)

range_color_min = []
range_color_max = []

for range_rgb in range_color:
    range_color_min.append(range_rgb[0])
    range_color_max.append(range_rgb[1])

tuple_color_max = tuple(map(int, range_color_max))
tuple_color_min = tuple(map(int, range_color_min))

print("Buscando valores entre: {} e {}".format(tuple_color_min, tuple_color_max))
    

color_to_change = (0, 100, 255)

pixels = img_to_scan.load()

for i in range(img_to_scan.size[0]):
    for j in range(img_to_scan.size[1]):
        if pixels[i, j] >= tuple_color_min and pixels[i, j] <= tuple_color_max:
            img_to_scan.putpixel((i, j), color_to_change)

img_to_scan.save("imgs/converted/coffee_scanned_img({}).jpg".format(time.time()))
img_to_scan.show()
