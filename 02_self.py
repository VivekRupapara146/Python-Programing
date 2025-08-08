class Employee:
    language = "Py"  #this is class attribute
    salary = 1200000
    
    def getInfo(self):    
        #giving self is important even if not used
        print(f"The language is {self.language} and salary is {self.salary}")
    
    def greet(self):
        print("Good morning")
        
    @staticmethod  #no need of object
    def bye():
        print("Goodbye! Have a nice day")
     

Rohan = Employee()
Rohan.name = "Rohan"
Rohan.language = "Javascript"  #this is instance atrribute
print(Rohan.name, Rohan.salary, Rohan.language)
Rohan.greet()
Rohan.getInfo()
Rohan.bye()

# gets converted to "Employee.getInfo(Rohan)" so if self not given as argument at the time of defining then it will give error of positional argument given
