class Rectangle:
    def __init__(self, base: float, height: float) -> None:
        self.__base = base
        self.__height = height
        
    def get_height(self) -> float:
        return self.__height
    
    #YOUDO the get_base method
    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    #Youdo get_area method
 
 
 
#YOUDO>  create two rectangles.  print their base, height, perimeter, and area
#using only the methods not the fields/property/attributes
