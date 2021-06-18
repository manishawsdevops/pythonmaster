# Overview of Scripting using Python.

# Image Processing in Python.

# Pillow is the standard library using the images with python.

from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# print(dir(img))
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = filtered_img.convert('L')
# # crooked = filtered_img.rotate(180)
# # crooked.save('smoothen_pikachu.png', 'png')
# # filtered_img.show()
# resize = filtered_img.resize((100, 100))
# resize.save('smallpika.png', 'png')


# Cropping the Image.
box = (100, 100, 400, 400)
region = img.crop(box)
region.save('cropped_pikachu.png', 'png')
