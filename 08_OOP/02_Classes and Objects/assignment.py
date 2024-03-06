from math import hypot, atan, degrees, pi

class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height   

    def area(self):
        return self.base * self.height
    
    def hypotenuse(self):
        return hypot(self.base, self.height)

    def perimeter(self):
        return self.base + self.height + self.hypotenuse()
    



triangle1 = RightTriangle(3, 4)
print("The area of triangle1 is", triangle1.area())


triangle2 = RightTriangle(30, 15)
print("The area of triangle2 is", triangle2.area())








# YOUDO: make another rightTriangle called triangle2
# YOUDO:  and print its area.