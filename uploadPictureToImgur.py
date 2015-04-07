__author__ = 'zyan'
import pyimgur

CLIENT_ID = "0ef99e9350b39b2"
PATH = "/home/zyan/PycharmProjects/PenrosePython/penrose.png"

im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
print(uploaded_image.title)
print(uploaded_image.link)
print(uploaded_image.size)
print(uploaded_image.type)