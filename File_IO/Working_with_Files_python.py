# Working with files in python.
# File I/O - Input Output

myfile = open('test.txt')

print(myfile)
print(myfile.read())
# # read() will read the entire file.
myfile.seek(0)
# # seek() will point the file to the respective line/position.
print(myfile.read())

print(myfile.readline())
# # readline() will read the single / first line.

print(myfile.readlines())
# readlines() will output the lines into the form a list of lines.

myfile.close()
# close() will close the file.
