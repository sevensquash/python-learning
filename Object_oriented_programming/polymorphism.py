from math import pi

class Shape:
    def __init__(self,color):
        self.color = color

    def area(self):
        return 0
    
    def describe(self):
        return f"I am a {self.color} shape."

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return pi * self.radius**2
    
class Square(Shape):
    def __init__(self,color,width):
        super().__init__(color)
        self.width = width

    def area(self):
        return self.width**2

class Triangle(Shape):
    def __init__(self,color,width,height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return 0.5 * self.height * self.width

class Rectangle(Shape):
    def __init__(self,color,width,height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width
    
def print_info(shape):
    print(shape.describe())
    print(f"area: {shape.area():.2f}")

print_info(Circle("red", 5))
print_info(Square("blue", 4))
print_info(Triangle("green", 6, 3))
print_info(Rectangle("yellow",4,5))