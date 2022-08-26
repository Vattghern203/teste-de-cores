import time

def save_image(img, name="img_{}".format(time.time()), format="jpg"):
    saved_img = img.save("imgs\saved\{}.{}".format(name, format))

    return saved_img


def image_matriz(img):
    cores = []
    for cor in img.getdata():
        if cor not in cores:
            cores.append(cor)

    return print(cores)

