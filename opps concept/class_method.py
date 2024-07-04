class Counting():
    count = 0  # class variable/ class attribute.

    def __init__(self, name, last, age):
        Counting.count += 1
        self.first_name = name
        self.last_name = last
        self.age = age

    @classmethod
    def from_string(cls, string):               #for creating instance in other way...
        first_name, last_name, age = string.split(',')
        return cls(first_name, last_name, int(age))

    @classmethod  # this is a decorator
    def count_instance(cls):
        return f"you have created {cls.count} instances of Counting class."


c1 = Counting('shivani', 'dubey', 20)
c2 = Counting('abhishek', 'dubey', 22)
c3 = Counting('saurabh', 'dubey', 25)
c4 = Counting.from_string('shivani,dubey,24')             #creating instance in other way...
print(c4.__dict__)
print(f"total instance are:- {Counting.count}")
print(Counting.count_instance())
