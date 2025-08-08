# Dunder methods let us define how objects behave with built in operations like +, len(), str(), comparisions etc. 
# Dunder = Double Underscore
# __methodName__()
# 

class Employee:
    language = "C++"  #this is class attribute
    salary = 1200000
    
    def __init__(self, name, salary, language): 
        #gets called  automatically when object is created
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
    
    def getInfo(self):    
        #giving self is important even if not used
        print(f"The language is {self.language} and salary is {self.salary}")
    
    def greet(self):
        print("Good morning")
        
    @staticmethod  #no need of object
    def bye():
        print("Goodbye! Have a nice day")

rohan = Employee("Rohan", 1300000, "Python")
# Rohan.name = "Rohan"
print(rohan.name, rohan.salary, rohan.language)

# Vivek = Employee() #gives error since no arguments passed