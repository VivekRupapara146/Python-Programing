class Employee:
    a = 1
    @classmethod
    def showClass(cls):
        print(f"Class attribute of a is {cls.a}")
    
    def show(self):
        print(f"instance attribute of a is {self.a}")

e = Employee()
e.a= 4
e.showClass()
e.show()