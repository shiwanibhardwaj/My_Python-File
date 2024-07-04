# Account details and salary increament.

class Account:
    def __init__(self, name, number, salary):
        Account.amount = 1000
        self.name = name
        self.number = number
        self.salary = salary

    @classmethod
    def string_access(cls, string):
        name, number, salary = string.split(",")
        return cls(name, number, int(salary))

    def salary_increament(self):
        if self.salary < 2000:
            self.salary += Account.amount
            return self.salary
        else:
            return f"your salary is {self.salary}"


p1 = Account.string_access("shivani ,8604726783,1000")
p1.salary_increament()
print(p1.__dict__)
