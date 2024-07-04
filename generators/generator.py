# Creation and Syntax :-
# Lists: Created using square brackets [] or the list() function.
my_list = [1, 2, 3, 4, 5]

# Generators: Created using parentheses () or the yield keyword in a function
my_generator = (x * x for x in range(5))


def my_generator_func():
    for x in range(5):
        yield x * x


# Evaluation :-
# Lists: Evaluated immediately. When a list is created, all elements are computed and stored
my_list = [x * x for x in range(5)]
# my_list is [0, 1, 4, 9, 16]

# Generators: Lazy evaluation. Elements are computed on the fly as they are requested
my_generator = (x * x for x in range(5))
# Elements are generated as you iterate over my_generator


# Iteration :-
# Lists: Can be iterated multiple times. Since all elements are stored in memory, you can loop through a list as many times as needed.
for x in my_list:
    print(x)
for x in my_list:
    print(x)

# Generators: Can be iterated only once. After a generator is exhausted, it cannot be reused unless explicitly recreated.
for x in my_generator:
    print(x)
for x in my_generator:
    print(x)  # This will not print anything since the generator is exhausted


# Example Comparison :-
# Here’s a direct comparison using both lists and generators:

# List
my_list = [x * x for x in range(5)]
print(my_list)  # Outputs: [0, 1, 4, 9, 16]

# Generator
my_generator = (x * x for x in range(5))
print(list(my_generator))  # Outputs: [0, 1, 4, 9, 16]

# Note: Converting the generator to a list with list(my_generator) will exhaust it.


def gen(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield i


num = gen(10)  # here we already generated .
for n in num:
    print(n)

for n in num:
    print(n)       # This will not print anything since the generator is exhausted


for n in gen(10):  # here we are generating so it will work
    print(n)

for n in gen(10):  # here we are generating so it will work
    print(n)
