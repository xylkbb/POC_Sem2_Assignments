# procedural approach
def calculate_area(width, height):
    return width * height


width = int(input('What is the width? '))
height = int(input('What is the height? '))
area = calculate_area(width, height)
print('The area is', area)


# procedural approach
def calculate_area(width, height):
    return width * height


width = int(input('What is the width? '))
height = int(input('What is the height? '))
area = calculate_area(width, height)
print('The area is', area)

age = int(input('Hey, and what is your age? '))
strange_operation = calculate_area(age, height)
print('Your age multiplied by the height is', strange_operation)


# object approach
class Rectangle:
    def __init__(self, width, height):
      self.width = width
      self.height = height

    def get_area(self):
        return self.width * self.height


a = int(input('What is the width? '))
b = int(input('What is the height? '))

rectangle = Rectangle(a, b)
print('The area is', rectangle.get_area())
