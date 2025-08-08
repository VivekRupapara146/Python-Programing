n1 = int(input("Enter number to start sum from: "))
n2 = int(input("Enter number till you want sum: "))
sum = 0
for n in range(n1, n2):
    sum += n
    
print(f"The sum of naturl numberes from {n1} to {n2} is {sum}")
