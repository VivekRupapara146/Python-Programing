class Employee():
    def __init__(self):
        print("Constructor of Employee")
    a= 1

class Programmer(Employee):
    b = 2
    def __init__(self):
       print("Constructor for Programmer")
    

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor for Manager")
    c = 3
    
# o = Employee()
# print(o.a) #print the a attribute
# # print(o.b) gevies an error

o = Programmer()
print (o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)