# Write a class Complex to represent complex numbers, along with overloaded opexators + and * which adds and multiplies them

class ComplexNo:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __str__(self):
        return (f"{self.real} + {self.imaginary}i")
    
    def __add__(self, other):
        return ComplexNo(self.real + other.real , self.imaginary + other.imaginary)
    
    def __mul__(self, other):
        realpart = (self.real*other.real)- (self.imaginary*other.imaginary)
        imaginarypart = (self.imaginary * other.real) + (self.real * other. imaginary)
        return ComplexNo(realpart , imaginarypart)

a = ComplexNo(5 , 3)
print(f"First complex number is {a}")
b= ComplexNo(2 , 6)
print(f"Second complex number is {b}")
c = a + b
print(f"The sum of a and b is {c}")
d = a * b
print(f"The multiplication of a and b is {d}")