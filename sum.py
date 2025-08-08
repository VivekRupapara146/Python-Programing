def sum_of_naturals(n):
    if n == 1:
        return 1
    return n + sum_of_naturals(n-1)

x  = int(input("Sum of how many natural numbers is required?\n"))

sum = sum_of_naturals(x)

print(f"The sum of first {x} natural numbers is {sum}")