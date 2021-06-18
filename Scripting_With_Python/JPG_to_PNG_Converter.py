# JPEG to PNG Formats.

# Grab the first and second argument as input from the terminal which are folder of images and
# new folder to be created
# Check if new folder exists if not create it.

# Loop throguh the Pokedex, Convert the images to png and save to new folder.

# Below code is written by me.

# import sys
# import os
# from PIL import Image
# import pdb


# def file_generator(*args, **kwargs):
#     for file in os.listdir(args[0]):
#         # if os.path.isfile(os.path.join(args[0], file)) and file.endswith('.jpg', '.jpeg'):
#         if file.endswith('.jpg') or file.endswith('jpeg'):
#             yield file


# def jpg_png_converter(*args, **kwargs):
#     try:
#         for file in file_generator(args[0]):
#             infile = (os.path.join(os.getcwd(), args[0], file))
#             outfile = (os.path.join(os.getcwd(), args[1], file))
#             f, e = os.path.splitext(outfile)
#             outfile = f + '.png'
#             with Image.open(infile) as im:
#                 im.save(outfile)
#     except Exception as err:
#         print(err)


# try:
#     if not os.path.exists(sys.argv[2]):
#         os.makedirs(sys.argv[2])
#     if os.path.exists(sys.argv[1]):
#         jpg_png_converter(sys.argv[1], sys.argv[2])
#     else:
#         print(f'{sys.argv[1]} doesnot exists')
# except OSError as err:
#     print(err)

import sys
import os
from PIL import Image

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{path}{filename}')
    # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
    img.save(f'{directory}/{clean_name}.png', 'png')
    print('all done!')
