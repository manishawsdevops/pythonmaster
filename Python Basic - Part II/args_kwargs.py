#*args and **kwargs

#These are the positional parametrs that we provide while invoking the function.
#These are key word parameters that we can provide while invoking the function as below.

#in the below example 1,2,3,4,5 are *args and num1=1,num2=2 is keyword paramter.
#So, args are tuple and kwargs is a dict.

#Rule for providing parameters in functions are
#params,*args,default parameters,**kwargs

def super_func(*args,**kwargs):
    print(args,kwargs)


super_func(1,2,3,4,5,num1=1,num2=4)

