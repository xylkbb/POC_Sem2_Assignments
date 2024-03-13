class Rectangle:
<<<<<<< HEAD
    __counter = 0

    def get_count():
        return Rectangle.__counter

    def __init__(self, base: float, height: float) -> None:
        self.__base = base
        self.__height = height
        Rectangle.__counter += 1


    def get_base(self) -> float: 
        return self.__base
    
    def get_height(self) -> float: 
        return self.__height    


    def area(self) -> float:
        return self.__base * self.__height

    def perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height

    def __str__(self) -> str:
        return "Rectangle of base:" + self.__base + ", height ", +self.__height



rect1 = Rectangle(5, 3)

rect2 = Rectangle(6, 8)
print("The base of rectangle 1 is", rect1.get_base())
print("The height of rectangle 1 is", rect1.get_height())
print("The area of rectangle 1 is ", rect1.area())
print("The perimeter of rectangle 1 is", rect1.perimeter())
print("_________________")
print("The base of rectangle 2 is", rect2.get_base())
print("The height of rectangle 2 is", rect2.get_height())
print("The area of rectangle 2 is", rect2.area())
print("The perimeter of rectnalge 2 is", rect2.perimeter())
print(Rectangle.get_count())
print("_________________")
=======

    def __init__(self, base: float, height: float) -> None:
        if (base < 0):
            self.__base = 0
        else:
            self.__base = base

        if (height < 0):
            self.__height = 0
        else:
            self.__height = height

    def get_height(self) -> float:
        return self.__height

    # YOUDO the get_base method

    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height

    # Youdo get_area method
    
    def __str__(self) -> str:
        #Rectangle with base:3, height:4
        return "Rectangle with base:" + str(self.__base) + ", height:" + str(self.__height)
    


# YOUDO>  create two rectangles.  print their base, height, perimeter, and area
# using only the methods not the fields/property/attributes
>>>>>>> 73a7eaf95d67ac9eec084cec55955e01fa981183
