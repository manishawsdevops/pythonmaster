# Best practice is to write try catch block.

try:
    with open('sad.txt') as myfile:
        print(myfile.readlines())
except FileNotFoundError as err:
    print('File not found error')
    # raise err
