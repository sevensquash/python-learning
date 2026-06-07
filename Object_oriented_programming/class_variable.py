class student:
    #class variable
    graduating_year = 2024
    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.num_students += 1

student1 = student("chole",15)
student2 = student("thierry",17)
student3 = student("jimmmy",16)
print(student1.name, student1.age, student1.graduating_year)
print(student2.name, student2.age,  student1.graduating_year)
print(student3.name, student3.age,  student1.graduating_year)

print(student.graduating_year)
print(student.num_students)

# Conclusion 

# class variable is shared among all the instances of a class and it is defined outside the constructor
# object student1,student2,student3 neither of them have graduating_year and num_students variable 
# so they fall back to class and finds class variable  
