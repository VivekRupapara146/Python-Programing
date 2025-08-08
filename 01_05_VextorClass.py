# Create a class 2dvector and use it to create another Class representing a 3-d vector

# class TwoDVector:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j
    
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j")

# class ThreeDvector(TwoDVector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k
    
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
    
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j + {self.k}k")
        
# m1 = TwoDVector(1,2)
# n1 = ThreeDvector(1, 2, 3)

# m1.show()
# n1.show()
# print(n1)

# write a class vector representing a vector of n dimension Overload + and * operator which calculates the sum and dot product respectively

class Vector:
    def __init__(self, components):
        self.components = components
    
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Length of both vectors must be same")
        v_sum = [a+b for a,b in zip(self.components, other .components)]
        return Vector(v_sum)

    def __str__(self):
        return f"Vector{self.components}"
    
    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Length of both vectors must be same")
        dproduct = sum(a*b for a,b in zip(self.components, other.components))
        return dproduct
    
    def __len__(self):
        return len(self.components)
    
v1 = Vector([int(x) for x in input("Enter components of vector seperated by commas: ").split(",")])

print(f"v1 is : {v1}")

v2 = Vector([int(x) for x in input("Enter components of vector seperated by commas: ").split(",")])

print(f"v2 is : {v2}")

v_sum = v1 + v2

print(f"Sum of v1 and v2 is {v_sum}")

dp = v1 * v2
print(f"Dot product of v1 and v2 is {dp}")

print(f"Length of the vector v1 is {len(v1)}\n")
print(f"Length of the vector v2 is {len(v2)}")