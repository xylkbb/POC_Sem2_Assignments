class Rectangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height
    


class Square(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)

