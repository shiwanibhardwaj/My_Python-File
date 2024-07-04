class Bank_Account():
    def __init__(self, name, account_No, balance=0.0):
        self.__account_holder_name = name
        self.__account_number = account_No
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    @property
    def check_balance(self):
        print(f"Current balance is {self.__balance}.")


s = Bank_Account("shivani", 8604726783, 700)
a = Bank_Account("abhshek", 8604727646, 1000)
print(a.__dict__)
a.check_balance
a.deposit(300)
a.withdraw(500)
print(a._Bank_Account__balance)          #we can access private members like this.  