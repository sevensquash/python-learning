class Employee:
    def __init__(self,name,profession):
        self.name = name
        self.profession = profession

    def info(self,name,profession):
        return f"{self.name} occupation is: {profession}"

    @staticmethod
    def is_available(profession):
        professions = ["manager","janitor","cook"]
        return profession in professions

employee = Employee("spongebob","cook")
print(employee.name, employee.profession)
print(f"is manager post avaiable : {Employee.is_available("manager")}")

class Student:
    count = 0
    average_gpa = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.average_gpa += gpa

    # instance method - passes the object itself
    def intro(self,name,gpa):
        return f"{name} scored {gpa}."
    
    #static method - passes nth speical but can be used to make utility things inside the class
    @staticmethod
    def is_alive():
        return True

    # class method - passes class itself
    @classmethod
    def count_student(clr):
        return f"Student count is: {clr.count}"

    @classmethod
    def average_gpa_count(clr):
        if clr.count == 0:
            return 0 
        else:
            return f"The average gpa of class is: {(clr.average_gpa / clr.count):.2f}"
        
student1 = Student("Spongebob",3.60)
student2 = Student("patrik",4.00)
student3 = Student("Sandy",4.00)

print(student1.name, student1.gpa)
print(student2.name, student2.gpa)
print(student3.name, student3.gpa)

print(student1.is_alive())

print(Student.count_student())
print(Student.average_gpa_count())

# magic method also dunder method
# they are automatically called by python built-in operators
# allows you to modify behaviour and output of object 

class Movie:

    def __init__(self,title,director,protagonist,movie_len):
        self.title = title
        self.director = director
        self.protagonist = protagonist
        self.movie_length = movie_len

    # called when print runs
    def __str__(self):
        return f"Movie name: {self.title}, Author name: {self.director}, Protagonist: {self.protagonist}, Duration: {self.movie_length}m"
    
    def __add__(self, other):
        duration_in_min = (self.movie_length + other.movie_length)
        hour= (self.movie_length + other.movie_length)//60
        minute = duration_in_min % 60
        return f"You need {hour}h and {minute}m to finish it in one sitting."
    
    def __gt__(self, other):
        if self.movie_length > other.movie_length:
            return f"{self.movie_length} is longer."
        else:
            return f"{other.movie_length} is longer."
        
    def __lt__(self, other):
        if self.movie_length < other.movie_length:
            return f"{self.movie_length} is shorter."
        else:
            return f"{other.movie_length} is shorter."
    
    def __eq__(self, other):
        if self.title == other.title and self.director == other.director:
            return f"both are same movie with different squeals by same director"
        else:
            return f"Different movies with different director"

    # key is the item you send so no need to self.key otherwise it would mean movie1.key
    # but movie1 doesnt have attribute key
    def __getitem__(self, key):
        if key == "title":
            return f"title : {self.title}"
        elif key == "director":
            return f"director : {self.director}"
        elif key == "movie_length":
            return f"movie length : {self.movie_length}"


movie1 = Movie("Project_hail_mary","Phil Lord and Christopher Miller","rayn gosling as grace",156)
movie2 = Movie("The martain","Ridely Scoot","Mark Watney as Matt Damon",91)

print(movie1)
print(movie2)

# dunder methods are called autmatically called when some specific function runs 
print(movie1 + movie2)
print(movie1 == movie2)
print(movie2["movie_length"])
print(movie1 > movie2)
print(movie1 < movie2)
