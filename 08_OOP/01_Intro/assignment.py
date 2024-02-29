class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        print("The area to tri1 is", self.base * self.height, "!!")
    def area2(self):
        print("The area to tri2 is", self.base * self.height, "!!")
         



tri1 = RightTriangle(1, 2)
tri2 = RightTriangle(4, 6)

print("The base to tri1 is ", tri1.base)
print("The height to tri1 is ", tri1.height)
tri1.area()
print( "\n")
print("The base to tri2 is ", tri2.base)
print("The height to tri2 is ", tri2.height)
tri2.area()