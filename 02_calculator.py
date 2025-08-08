class Calculator():
    def __init__(self, value):
        self.value = value
    
    def square(self):
        sq = self.value ** 2
        print(f"Square of {self.value} is : {sq:.2f}")
    
    def cube(self):
        cu = self.value ** 3
        print(f"Cube of {self.value} is : {cu:.2f}")
    
    def squareroot(self):
        sqr = self.value ** 0.5
        print(f"Squareroot of {self.value} is : {sqr:.2f}")
    

a = Calculator(float(input("Enter a number: ")))

operation = int(input("Slect operation:\n1. Square\n2. Cube\n3. Sqare root\n"))
if operation == 1:
    a.square()
elif operation == 2:
    a.cube()
elif operation == 3:
    a.squareroot()
else: print("Invalid input")