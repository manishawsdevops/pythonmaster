# File Paths in Python - How to provide the file paths in python.
# We can provide Absolute Path or Relative path

with open('./app/sad.txt') as myfile:
    print(myfile.readlines())

# This is dependent on the operating system and the respective paths.

# We are having library called Pathlib.
# This is useful for the both the operating systems.
