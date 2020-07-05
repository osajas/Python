from PIL import Image, ImageFilter

img = Image.open('./Pokemon/original.jpg')
print(img.size)
new_image = img.resize((400, 400))
new_image.save("astro.jpg")
print(new_image.size)
img.thumbnail((400, 400))
img.save("thumbnail.jpg")
print(img.size)