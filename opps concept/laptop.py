# class Laptop:
#     def __init__(self, brand, model, price):
#         self.brand_name = brand
#         self.model_name = model
#         self.price = price
#         self.model_or_name = brand+' '+model

#     def apply_discount(self, num):
#         off_price = (num/100)*self.price
#         return self.price-off_price


# L1 = Laptop("asus", "watelfall", 78000)
# L2 = Laptop("dell", "Inspiron", 55000)
# print(L1.__dict__)
# print(L2.__dict__)
# print(L1.apply_discount(20))
# print(L1.apply_discount(50))


class Laptop:
    discount = 20                   

    def __init__(self, brand, model, price):
        self.brand_name = brand
        self.model_name = model
        self.price = price
        self.model_or_name = brand+' '+model

    def apply_discount(self):
        off_price = (self.discount/100)*self.price
        return self.price-off_price


L1 = Laptop("asus", "watelfall", 780000)
print(L1.__dict__)
print(L1.apply_discount())


L2 = Laptop("dell", "Inspiron", 55000)
L2.discount = 50
print(L2.__dict__)
print(L2.apply_discount())
