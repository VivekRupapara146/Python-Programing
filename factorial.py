n = int(input("Enter number to find fatorial of: "))

fact = 1
for i in range(2, n+1):
    if n < 2 : break
    fact = fact*i
        
print(f"Factorial of {n} is {fact}")
