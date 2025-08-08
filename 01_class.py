class Employee:
    language = "Py"  #this is class attribute
    salary = 1200000

Rohan = Employee()
Rohan.name = "Rohan"
Rohan.language = "Javascript"  #this is instance atrribute
print(Rohan.name, Rohan.salary, Rohan.language)

Vivek = Employee()
Vivek.name = "Vivek G Rupapara"
print(Vivek.name, Vivek.salary, Vivek.language)

# here name is an object attribute and salary/language are class atrribute as they directly belong to the class

# instance attribute get preference over class attribute

