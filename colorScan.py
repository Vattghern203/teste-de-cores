from main import Image, ImageOps, save_image, rgb_to_hsv
import time

# Definindo a imagem a ser analisada
img_to_scan = Image.open(r"imgs/samples/coffee_original.jpg").convert('RGB')

# Definindo a amostra para a obtenção do range de cores
img_sample = Image.open(r"imgs/samples/coffee_sample.png").convert('RGB')

# Atribuindo o range de cores da imagem
range_color = img_sample.getextrema()

print("Máximos e mínimos dos valores RGB da amostra de cor:", range_color)

# Criando um array para separar os valores da tupla
range_color_min = []
range_color_max = []

for range_rgb in range_color:
    range_color_min.append(range_rgb[0])
    range_color_max.append(range_rgb[1])

# convertendo para tupla
tuple_color_max = tuple(map(int, range_color_max))
tuple_color_min = tuple(map(int, range_color_min))

print("Buscando valores entre: {} e {}".format(tuple_color_min, tuple_color_max))
    
# Valor RGB da cora a ser trocada
color_to_change = (0, 100, 255)

# Alocando os valores de pixel da imagem na variável
pixels = img_to_scan.load()

# Analisando os valores da imagem para encontar os que estão dentro do range e logo após colorí-los com a cor escolhida
for i in range(img_to_scan.size[0]):
    for j in range(img_to_scan.size[1]):
        if pixels[i, j] >= tuple_color_min and pixels[i, j] <= tuple_color_max:
            img_to_scan.putpixel((i, j), color_to_change)

# Salva a image em uma nova pasta para análise futura
img_to_scan.save("imgs/converted/coffee_scanned_img({}).jpg".format(time.time()))
img_to_scan.show()
