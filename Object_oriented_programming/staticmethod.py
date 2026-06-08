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