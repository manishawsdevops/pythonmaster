#Walrus Operator.
#:= - This is the walrus operator. We can use this to assign a variable to long expressions while
#evaluating . Below is the example.

a = 'Manish Gandhi Dodda'

if (n := len(a)) > 10:
    print(f'Too long for {n} characters.')

while (n := len(a)) > 1:
    print(n)
    a = a[:-1]