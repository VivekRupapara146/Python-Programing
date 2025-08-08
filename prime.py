x = int(input("Enter a number: "))
i=1
fact = []

for i in range(i, x+1):
     if x % i == 0:
        fact.append(i)

if len(fact)==2:
    print(f"\n{x} is a prime number.")
else:
    print(f"\n{x} is not a prime number with factors {fact}.")
