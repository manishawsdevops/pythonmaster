# Processing the Images.

# How to fix the aspect ratio. If we want to keep the aspect ratio as it is.
# We can use the thumbnail option.
# Thumbnail modifies the actual image.
# Thumbnail cannot be over 400 to 400.

from PIL import Image

img = Image.open('unsplash.jpg')
img.thumbnail((400, 400))
img.save('upsplash.jpg')
