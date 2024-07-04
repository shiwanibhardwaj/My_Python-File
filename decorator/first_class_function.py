# Assigning a function to a variable
def greet(name):
    return f"Hello, {name}!"


say_hello = greet
print(say_hello("Alice"))  # Output: Hello, Alice!

# Passing a function as an argument


def call_function(func, arg):
    return func(arg)


print(call_function(greet, "Bob"))  # Output: Hello, Bob!

# Returning a function from another function


def create_greeting_function(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet


hello_greet = create_greeting_function("Hello")
hi_greet = create_greeting_function("Hi")

print(hello_greet("Charlie"))  # Output: Hello, Charlie!
print(hi_greet("Dave"))        # Output: Hi, Dave!

# Storing functions in a list
function_list = [greet, hello_greet, hi_greet]
for func in function_list:
    print(func("Eve"))
