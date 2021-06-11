#While loops.
# while <if condition>:

#break will come out of the while loop.

i = 0
while i < 50:
    print(i)
    i += 1
    break
else:
    print("All the work is done")

#If we include break in the While loop, else part will not be executed. Else will only be 
#executed when there is no break in the while loop.

while True:
    response = input('Say something: ')
    if (response == 'bye'):
        break

