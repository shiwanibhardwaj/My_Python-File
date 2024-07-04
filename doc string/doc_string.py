#what is doc strings.
# how to write doc strings.
#how to see doc strings.
#what is help function.
def add(a,b):
    '''this function takes 2 numbers and returns their sum'''
    return a+b
print(add.__doc__)
#len,sum,max,min,sorted etc.
print(sum.__doc__)
print(max.__doc__)
print(min.__doc__)
print(sorted.__doc__)


#help...
print(help(sum))            #help function helps you to know about given functions.                     