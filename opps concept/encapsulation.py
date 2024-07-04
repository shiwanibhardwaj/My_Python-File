class Employee:
    amount = 2000

    def __init__(self, name, age, salary):
        self.name = name  # (public)
        self._age = age  # naming conversion. #(protected)
        self.__salary = salary  # name mangling.#(private)

    def welcome(self):
        return print(f"welcome to this company {self.name}.")

    def _increament(self):
        if self._age > 25:
            self.__salary += Employee.amount
            return print(f"your salary increamented by {Employee.amount},now your total salary is {self.__salary}")
        else:
            return print("sorry, no increament you are under 25.")

    def __info(self):
        print(self.__dict__)


e1 = Employee('shivani', 20, 2000)
e2 = Employee('saurabh', 26, 3000)
e3 = Employee('abhishek', 23, 3000)

e1.welcome()
e1._increament()
e1._Employee__info()
print(f"The employee name is: {e1.name}")
print(f"The employee age is: {e1._age}")
print(f"The employee salary is: {e1._Employee__salary}")


e2.welcome()
e2._increament()
e2._Employee__info()
print(f"The employee name is: {e2.name}")
print(f"The employee age is: {e2._age}")
print(f"The employee salary is: {e2._Employee__salary}")


e3.welcome()
e3._increament()
e3._Employee__info()
print(f"The employee name is: {e3.name}")
print(f"The employee age is: {e3._age}")
print(f"The employee salary is: {e3._Employee__salary}")
e3._age = 27
print(f"The employee age is: {e3._age}")
e3._increament()
