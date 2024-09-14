

def devide(a, b):
    try:
        return print(a/b)
    except ZeroDivisionError:
        print("please,don't devide by zero")
    except TypeError as e:
        print(e)


devide(2, "0")
