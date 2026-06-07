#Intro object oriented programming

class car:
    def __init__(self,model,year,for_sale):
        self.model = model 
        self.year = year
        self.for_sale = for_sale

    def drive(self):
        print(f"{self.model} can drive!")
    def honk(self):
        print(f"{self.model} can honk!")
    def accelerate(self):
        print(f"{self.model} can accelerate!")

car1 = car("Mustang",2025,False)
print(f"{car1.model} is a very good car")
print(f"Its year is: {car1.year}")
print(f"for sale: {car1.for_sale}")
car1.drive()
car1.honk()
car1.accelerate()

car2 = car("corvette",2023,False)
print(f"{car2.model} is a very good car")
print(f"Its year is: {car2.year}")
print(f"for sale: {car2.for_sale}")
car2.drive()
car2.honk()
car2.accelerate()

# class is like a blueprint for an object construction. Constructor is automatically called when an object
# is created. __init__ is a constructor and self is provided as parameter automatically which is equal to
# the variable it is calling using attribute access operator (.) and objects attributes are stored in type 
# of dictinoary and method lives in the class itself while attributes live inside the constructor.

