# raise error example 2 :-

class Mobile:
    def __init__(self, name):
        self.name = name


class MobileStore():
    def __init__(self):
        self.mobiles = []

    def add_mobiles(self, new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("new_mobile should be object of Mobile class.")


oneplus = Mobile("samsung")
redmi = "redmi promax"
mobileStore = MobileStore()
print(mobileStore.mobiles)
mobileStore.add_mobiles(oneplus)
print(mobileStore.mobiles)
mobo_phone = mobileStore.mobiles
print(mobo_phone[0].name)
