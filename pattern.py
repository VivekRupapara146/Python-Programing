'''
*
**
***

  *
 ***
*****

***
* *
***

  *
 * *
*****

 

'''

n = int(input("Enter number of rows: "))
print("pattern 1: \n")
# for i in range(1, n+1):
#     stars = i
#     print("*" * stars)
    
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()

print("pattern 2: \n")

for i in range(1, n+1):
    spaces = n - i
    stars = (2*i)-1
    print(" " * spaces + "*" * stars)

print("pattern 3 using 2 variables: \n")

for i in range(1, n+1):
    if i==1 or i==n:
        print("*" * n)
        continue
    else:
        spaces = n - 2
        print("*" + " " * spaces + "*")

print("pattern 3 using matrix travesal or nested for loop: \n")

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("*" , end="")
        else:
            print(" ", end="")
    print()

print("pattern 4: \n")

x = int(input("Enter no of rows for hollow pyramid: "))

for i in range(x):
    for space in range(x-i-1):
        print(" ", end="")
        
    for j in range((2*i)+1):
        if j == 0 or i == x -1 or j == 2*i:
            print("*", end="")
        else:
            print(" ", end="")
    print()