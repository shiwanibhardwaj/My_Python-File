"""
Exception handling in Python is a way to handle errors that occur during the execution of a program,
allowing the program to continue running or to terminate gracefully. 
Instead of stopping the program immediately,
Python allows you to catch and manage these exceptions.
This is done using the try, except, else, and finally blocks.

"""


try:
    l = [1, 2, 3, 4]
    print(l[6])
except IndexError:
    print("index out of range.")
except Exception as e:
    print(f"An error occurred: {e}")
    """ Exception is the base class for all built-in exceptions, so this will catch any other error types.
  The variable e captures the exception object, and the message "An error occurred: {e}" is printed, 
  which includes the details of the exception.
  """


x = 29/0
try:
    x = 29/0
except ZeroDivisionError:
    print("can't  devide by zero.")


while True:
    try:
        age = int(input("enter your age :"))
        break
    except ValueError:
        print("may be you entered string or something instead of number,try again.")
    except:
        print("unexpected error")

if age < 18:
    print("you can't play this game.")
else:
    print("you can play this game.")


# Raising Exceptions..

def positive(num):
    if num < 0:
        raise ValueError("number must be positive.")
    return num


try:
    positive(-3)
except ValueError as e:
    print(e)


# Custom Exceptions.
# You can define your own exceptions by creating a new class that inherits from the built-in Exception class.

class CustomError(Exception):
    pass


try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(e)
