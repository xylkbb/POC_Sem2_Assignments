from math import hypot, atan, degrees


class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.small_angle = atan(self.height / self.base)
        self.small_angle = degrees(self.small_angle)
        self.large_angle = atan(self.base / self.height)
        self.large_angle = degrees(self.large_angle)
        small = self.small_angle
        large = self.large_angle
        self.small_angle = min(small, large)
        self.large_angle = max(small, large)       
        

    def area(self):
        # Youdo return the area which is 1/2 * base * height
        pass  # Remove this pass when finished

    def hypotenuse(self):
        return hypot(self.base, self.height)

    def perimeter(self):
        return self.base + self.height + self.hypotenuse()


triangle1 = RightTriangle(3, 4)
print("The area of triangle1 is", triangle1.area())
print("The hypotenuse of triangle1 is", triangle1.hypotenuse())
print("The perimeter of triangle1 is", triangle1.perimeter())
print("The perimeter of triangle1 is", triangle1.perimeter())
print("The small angle of triangle1 is", triangle1.small_angle)
print("The large angle of triangle1 is", triangle1.large_angle)



# YOUDO: make another rightTriangle called triangle2
# YOUDO:  and print its area.
