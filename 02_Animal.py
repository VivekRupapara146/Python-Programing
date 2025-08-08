# Create a class pets from a class Animals and further create class Dog from Pets. Add a method bark to class Dog

class Animals:
    def __init__(self):
        pass
    def category(self):
        print(f"{self} is an animal")
        
    def __str__(self):
        return self.__class__.__name__

class Pets(Animals):
    def __init__(self):
        super().__init__()
    
    def type(self):
        print(f"{self} is a Pet")

class Dog(Pets):
    def __init__(self):
        super().__init__()
    
    def species(self):
        print(f"{self} is a Dog")
    
    @staticmethod
    def bark():
        print("The dog is barking")
        
A = Animals()
A.category()

B = Pets()
B.category()
B.type()

C = Dog()
C.category()
C.type()
C.species()
C.bark()