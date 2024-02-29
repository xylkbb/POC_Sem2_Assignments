class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def CalculateArea(self):
        print("The area is", self.base * self.height, "!!")



righttriangeone = RightTriangle(1, 2)
righttriangetwo = RightTriangle(4, 6)

righttriangeone.CalculateArea()
righttriangetwo.CalculateArea()
