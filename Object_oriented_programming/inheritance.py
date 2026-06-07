# interitance = allows a class to inherit attributes and methods form another class 
#               Helps with code reusability and extensibility
#               class child(Parent)
# multiple inheritance = inherit form more than one parent
#                        c(a,b)
# multi-level inheritance = child inherits from parent and grandparent
#                           c(b) <- b(a) <- a
# super() = Function used in a child class to call methods from a parent class (superclass).
# Allows you to extend the functionality of the inherited methods

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} can eat!")

    def sleep(self):
        print(f"{self.name} can sleep!")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} can flee!")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} can hunt!")

class Wolf(Predator):
    def speak(self):
        print("WOOF!")

class Bird(Prey,Predator):
    def speak(self):
        print("CHRIP!")

class Mouse(Prey):
    def speak(self):
        print("SQUEAK!")

wolf1 = Wolf("Luna")
bird1 = Bird("chuntaro")
mouse1 = Mouse("jerry")

print(f"{wolf1.name} is alive: {wolf1.is_alive}")
print(f"{bird1.name} is alive: {bird1.is_alive}")
print(f"{mouse1.name} is alive: {mouse1.is_alive}")

wolf1.speak()
wolf1.hunt()

bird1.speak()
bird1.flee()
bird1.hunt()

mouse1.speak()
mouse1.flee()

class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"{self.name} is a 2d geometry!")

class Circle(Shape):
    def __init__(self,name,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.name = name
        self.raduis = radius
    
    def describe(self):
        print(f"{self.color} circle with radius {self.raduis}cm its area is {pi*self.raduis**2:.2f}cm^2")


class Square(Shape):
    def __init__(self,name,color,is_filled,width):
        super().__init__(color,is_filled)
        self.name = name
        self.width = width

    def describe(self):
        super().describe()
        print(f"{self.color} square with width {self.width}cm its area is {self.width**2:.2f}cm^2")

class Triangle(Shape):
    def __init__(self,name,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.name = name
        self.width = width
        self.height = height

circle = Circle("circle","Blue",True,5)
square = Square("square","Red",True,6)
triangle = Triangle("triangle","green",True,5,6)
from math import pi

circle.describe()
square.describe()
print(f"{triangle.color} triangle with width {triangle.width}cm and height {triangle.height}cm its area is {0.5*triangle.width*triangle.height}cm^2")

#polymorhphism and duck typing

class cannis:
    def speak(self):
        print("rufff")

class felline:
    def speak(self):
        print("meow")

class naja:
    def speak(self):
        print(f"{self}: hisss")

def make_sound(animal):
    x = animal
    x.speak()
    
make_sound(cannis())
make_sound(felline())
make_sound(naja())