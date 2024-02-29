import math

class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        #YOUDO:  return the area of a right triangle from the formula. 
        pass #remove when done. 
    
    def hypotenuse(self):
        return math.hypot(self.height * self.base)
    
    def perimeter(self):
        return self.base + self.height + self.hypotenuse
    
    
tri1 = RightTriangle(3, 4)
print("The base of tri1 is", tri1.base)
# print("The height of tri1 is", tri1.height)
print("The area of tri1 is", tri1.area())
#YOU make another and print its area.  


    

