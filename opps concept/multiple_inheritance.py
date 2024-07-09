class Animal:
    def make_sound(self):
        print("Some sound")


class Dog:
    def make_sound(self):
        print("Bark")


class Cat(Animal, Dog):  # it will follow method resolution order.
    pass


c = Cat()
c.make_sound()
# mro method will show method resolution order of any class.we can also check like this (print(Cat.__mro__)). or by using help function.
print(Cat.mro())
print(Cat.__mro__)
print(help(Cat))
