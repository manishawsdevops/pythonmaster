# we have break,continue,pass in the Python to handle our programs.

#Break - this will come out of the loop.
#Continue - This will go to the start of the loop.
#Pass - This absolutely does nothing. It just pass the control to the next line of code.

#Break example.

mylist = [1,2,3]

for i in mylist:
    print(i)
    break

i = 0
while i < len(mylist):
    print(i)
    i += 1
    break


#Continue Example
for i in mylist:
    continue
    print(i)

i = 0
while i < len(mylist):
    i += 1
    continue
    print(i)


