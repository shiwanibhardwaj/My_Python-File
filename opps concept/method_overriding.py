# method overriding

class Animal:
    def make_sound(self):
        print("Some sound")


class Dog(Animal):
    def make_sound(self):
        print("Bark")


# Create an instance of Animal and call make_sound
animal = Animal()
animal.make_sound()  # Output: Some sound

# Create an instance of Dog and call make_sound
dog = Dog()
dog.make_sound()  # Output: Bark                (this is called method overriding.)
