# Read, Write, Append using Python.
# We dont need to close the file everytime. We need to use the below type of the code.

with open('test.txt') as myfile:
    print(myfile.readlines())

# By default the file will be opened in the read mode which is mode = 'r'
# To open in read and write mode use 'r+'
# Character	Meaning
# 'r'	open for reading (default)
# 'w'	open for writing, truncating the file first
# 'x'	create a new file and open it for writing
# 'a'	open for writing, appending to the end of the file if it exists
# 'b'	binary mode
# 't'	text mode (default)
# '+'	open a disk file for updating (reading and writing)

# When we use 'r+' it will write the text from the starting.
# If we use append mode it will add at the end of the mode.
# 'w' mode will update the file completly by deleting everything what present in the file.

with open('test.txt', mode='a') as myfile:
    myfile.write('I am writing the file using python')

with open('sad.txt', mode='w') as myfile:
    myfile.write(':-(')
