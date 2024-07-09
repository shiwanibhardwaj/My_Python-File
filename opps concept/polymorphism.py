# operator overloading.(differente work for same operator.)

b = 3
c = 6
a = print(b+c)   # here + sign will add two or more intigers.
string = print("shivani" + "dubey")  # here it will concatenate strings.
# here it will merge two or more lists. output :- [2,3,4,6,7,8,9]
l = print([2, 3, 4] + [6, 7, 8, 9])


# special magic methods / dunder methods

# __str__
# __repr__

class Hello:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"({self.name}, {self.age}  thank you.)"

    def __repr__(self):
        return f"Hello(\"{self.name}\", {self.age})"

    def __len__(self):
        return len(self.name)

    def __div__(self, a, b):
        return a/b

    def __add__(self, other):
        return self.name + " " + other.name


hello = Hello("shivani", 20)
hello1 = Hello("shiva", 28)
print(hello)
print(repr(hello))
print(hello.__repr__())
print(hello.__len__())
print(hello.__div__(3, 5))
print(hello+hello1)
