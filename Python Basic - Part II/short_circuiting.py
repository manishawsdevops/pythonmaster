#Short circuiting.

#short ciruiting majorly explains like if there is an operation of and, if the first conditions is False.
#Python interpreter will not check for the second condition after and, because anyway it is going to skip the
#statement. It is the same with or condition as well.
#The process of skipping the coditions validation is called as short circuiting.

if_friend = True
is_user = True

if if_friend and is_user:
    print('Baahubali is released')
