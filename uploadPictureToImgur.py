__author__ = 'zyan'
import pyimgur

CLIENT_ID = "8e6cf031726addc"
PATH = "/home/zyan/PycharmProjects/PenrosePython/penrose.png"

im = pyimgur.Imgur(CLIENT_ID)
# uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
uploaded_image = im.upload_image(PATH, title="Uploaded11")
gallery_image = im.create_album(title="penrosetill",images=uploaded_image.id)
# author = gallery_image.author
# print(gallery_image._INFO_URL)
# print(author.name)
print(uploaded_image.title)
print(uploaded_image.link)
print(uploaded_image.size)
print(uploaded_image.type)
print(uploaded_image.id)
print(uploaded_image.name)

# imm = pyimgur.Imgur(CLIENT_ID)
# image = imm.("Uploaded11")
# print(image.title) # Cat Ying & Yang
# print(image.link) # http://imgur.com/S1jmapR.jpg