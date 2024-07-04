#function with all parameters.

#parameters.
#*args.
#default parameter.
#**kwargs.

#order of parameters in function.(padk)

def fun(name,*args,last_name='unknown',**kwargs):   #if we change the order of parameters it will give error.
    print(name)
    print(*args)
    print(last_name)
    print(kwargs)

fun('shivani',1,2,3,4,first_name='unknown',age=20,village='fully')