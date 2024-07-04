class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name_(self):
        return f'{self.first_name} {self.last_name}'


class Student(Person):
    def __init__(self, first_name, last_name, age, mark, Class, gender):
        # two ways to inharete any class.
        # Person.__init__(self, first_name, last_name, age)    # uncomman way
        super().__init__(first_name, last_name, age)

        self.mark = mark
        self.Class = Class
        self.gender = gender


P1 = Person('shivani', 'dubey', 16)
print(P1.full_name_())
print(P1.__dict__)


p2 = Student("abhishek", "dubey", 23, 70, "bca", "male")
print(p2.full_name_())
print(p2.__dict__)
print(p2.age)
print(p2.first_name)
print(p2.last_name)
