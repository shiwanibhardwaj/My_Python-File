# multi level inheritence
# method resolution order.


# multi level inheritence


class Phone:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Smartphone(Phone):
    def __init__(self, name, price, brand, color):
        super().__init__(name, price)
        self.brand = brand
        self.color = color

    @property
    def show_info(self):
        print(self.__dict__)


class Laptop(Smartphone):
    discount = 30

    def __init__(self, name, price, brand, color, ram, rom):
        super().__init__(name, price, brand, color)
        self.ram = ram
        self.rom = rom

    def apply_discount(self):
        off_price = (self.discount/100)*self.price
        return self.price-off_price


phone = Phone("nokia", 500)
print(phone.__dict__)

smartphone = Smartphone("samsung galaxy", 22000, "samsung", "sky blue")
smartphone.show_info
print(smartphone.name)

laptop = Laptop("asus", 60000, "asus", "grey", "16 gb", "265 gb")
laptop.show_info
print(f"discount is: {laptop.apply_discount()}")
print(laptop.name)


# method resolution order.

help(Smartphone)          #it will show method resolution order.

