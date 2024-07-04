class shape_area:
    pi = 3.14

    def __init__(self, redius):
        self.redius = redius

    def circle_area(self):
        return shape_area.pi*self.redius*self.redius

    def square_area(self, a):
        return a*a

    def rectangle_area(self, w, l):
        return w*l


c1 = shape_area(20)
print(c1.circle_area())
print(c1.square_area(5))
print(c1.rectangle_area(5, 5))  
