class Phone:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    # The @property decorator defines the attribute method as the getter.
    @property
    def full_info(self):
        if self.name == None or self.brand == None:
            return f"full_info is not avalaible"
        return f"{self.name} {self.brand}"

    @full_info.setter
    def full_info(self, string):
        names = string.split("12")[0]
        self.name, self.brand = names.split(".")

    @full_info.deleter
    def full_info(self):
        self.name = None
        self.brand = None


p = Phone("samsung", "none", 34000)
p.brand = "mnc"
print(p.full_info)

p.full_info = "redmi.promax123@"
print(p.full_info)
print(p.name)
print(p.brand)

del p.full_info
print(p.full_info)
print(p.name)
print(p.brand)


class Service:

    def __init__(self, travel, food, game):
        self.travel_place = travel
        self.food = food
        self.game = game

    @property
    def travel_info(self):
        return print(f"Travel places :- {self.travel_place}")

    @property
    def game_info(self):
        return print(f"Games :- {self.game}")

    @property
    def food_info(self):
        return print(f"Food items :- {self.food}")


g = ["sppining tops", "football", "cricket"]
t = ["varanasi", "delhi", "panjab", "bihar", "kashmir"]
f = ["panir", "kabab", "allu paratha", "maggy"]

s = Service(t, f, g)
s.travel_info
s.game_info
s.food_info


# class MyClass:
#     def __init__(self):
#         self._attribute = None

#     @property
#     def attribute(self):
#         # This is the getter method
#         return self._attribute

#     @attribute.setter
#     def attribute(self, value):
#         # This is the setter method
#         if value < 0:
#             raise ValueError("Value cannot be negative")
#         self._attribute = value

#     @attribute.deleter
#     def attribute(self):
#         # This is the deleter method
#         del self._attribute

# # Example usage
# obj = MyClass()
# obj.attribute = 10  # Calls the setter method
# print(obj.attribute)  # Calls the getter method, outputs 10
# del obj.attribute  # Calls the deleter method
