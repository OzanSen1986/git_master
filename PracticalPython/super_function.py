class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    
    def area(self):
        return f'Area of square: {self.length * self.width} cm2'


class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    
    def volume(self):
        return f'Volume of cube: {self.length * self.width * self.height} cm3'


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())

