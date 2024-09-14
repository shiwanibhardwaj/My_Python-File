class Animal():
    def __init__(self,name):
        self.name=name
    
    def sound(self):
        raise NotImplementedError("you have to define this method in subclasses!")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed

    # def sound(self):
    #     print("bhoaw","bhoaw")

class Cat(Dog):
    def __init__(self,name,breed):
        super().__init__(name,breed)

    def sound(self):
        print("meaow","meaow")


dog=Dog("Tillu","lebra dog")
dog.sound()