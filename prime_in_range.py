x1 = int(input("Enter first number: "))
x2 = int(input("Enter second number: "))

prime = []

# for n in range (x1, x2+1):
#     fact = []
#     for i in range(1 , n+1):
#         if n  %  i == 0:
#             fact.append(i)
#     if len(fact)==2:
#         prime.append(n)

for n in range(x1, x2+1):
    if n<2: continue
    is_prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime  = False
            break
    if is_prime: prime.append(n)

print(f"List of prime numbers between {x1} and {x2} is {prime}")