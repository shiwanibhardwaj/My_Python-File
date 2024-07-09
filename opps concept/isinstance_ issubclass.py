# Define the base class
class Animal:
    def sound(self):
        print("This is a generic animal sound")

# Define a subclass that inherits from Animal


class Mammal(Animal):
    def sound(self):
        super().sound()  # Call the superclass's method
        print("Mammals make various sounds")

# Define another subclass that inherits from Mammal


class Dog(Mammal):
    def sound(self):
        super().sound()  # Call the superclass's method
        print("Woof woof")


dog = Dog()
mammal = Mammal()

# it will check that dog is an object of Dog class or not. if it's then print true.
print(isinstance(dog, Dog))
print(isinstance(dog, Mammal))  # it will give true because of inheritence.
print(isinstance(mammal, Dog))    # it will print false .


# it will check that dog is subclass of Animal class or not.
print(issubclass(Dog, Animal))
# it will check that dog is subclass of Mammal class or not.
print(issubclass(Dog, Mammal))
# it will check that Animal is subclass of Dog calss or not.
print(issubclass(Animal, Dog))
# it will check that Animal is subclass of Mammal calss or not.
print(issubclass(Animal, Mammal))
