class Employee:
    company = "ITC"
    id = 1
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is{self.salary}")

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name of the programmer is {self.name} and language is {self.language}")
        
a = Employee()
b = Programmer()

print(a.company, b.company, a.id, b. id)