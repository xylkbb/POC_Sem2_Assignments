from math import hypot

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


tri1 = RightTriangle(3, 4)
tri2 = RightTriangle(4, 6)

print("The base of triangle 1 is", tri1.base, "and", tri1.height, "\nThe area is", tri1.area())
print("The hypotenuse is", tri1.hypotenuse())
print("The perimeter is ", tri1.perimeter())

print("----------------------")

print("The base of triangle 2 is", tri2.base, "and", tri2.height, "\nThe area is", tri2.area())
print("The hypotenuse is", tri2.hypotenuse())
print("The perimeter is ", tri2.perimeter())


