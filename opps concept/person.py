class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name_(self):
        return f'{self.first_name} {self.last_name}'

    def is_above_18(self):
        if self.age > 18:
            return print("congratulations ,you are above 18.")
        else:
            return print("sorry, you are under 18.")


P1 = Person('shivani', 'dubey', 16)
print(P1.__dict__)
print(P1.full_name_())
P1.is_above_18()

P2 = Person('abhishek', 'dubey', 23)
print(P2.__dict__)
print(P2.full_name_())
P2.is_above_18()
