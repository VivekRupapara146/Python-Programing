class Number:
    def __init__(self, n):
        self.n = n
    
    def __add__(self, other):
        return self.n + other.n
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.y, self.y + other.y)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
            
n = Number(2)
m = Number(5)

print(n)
print(m) #for example of error
print(n + m)

p1 = Point(2, 3)
p2 = Point(3, 6)

p3 = p1 + p2
print(p3)