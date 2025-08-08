def maximum(a, b, c):
    if a > b:
        if a > c:
            return f"Number {a} is maximum"
        else:      #c > a
            return f"Number {c} is maximum"
    else:          #b > a
        if b > c: 
            return f"Number {b} is maximum"
        else:      #c > b
            return f"Number {c} is Maximum"


a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

print("Finding max of the given numbres: ")
print("-" * 50)
maximum(a, b, c)