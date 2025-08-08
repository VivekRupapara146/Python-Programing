# Create a class Employee and add salary and increment properties to it
# Write a method SalaryAfterIncrement, method with a @property decorator with a setter which changes the value of increment based on the salary

class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment
    
    @property
    def SalaryAfterIncrement(self):
        return self.salary + self.salary*(self.increment/100)
    
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, desired_salary):
        if desired_salary < self.salary:
            raise ValueError("Desired salary can not be less than original salary")
        self.increment = ((desired_salary - self.salary)/self.salary) * 100
        

A = Employee(50000, 5)

print(f"Employee salary: {A.salary}")
print(f"Increment percentage: {A.increment}%")
print(f"Updated Salary = {A.SalaryAfterIncrement}")

# A.increment = 8

# print(f"Updated Salary = {A.SalaryAfterIncrement}")

A.SalaryAfterIncrement = int(input("Enter desired salary amount(must be greater than original salary)"))

print(f"New Increment: {A.increment}")
print(f"Updated Salary = {A.SalaryAfterIncrement}")