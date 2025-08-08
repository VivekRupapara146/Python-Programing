x = int(input(f"Enter a number to obtain its table: "))

print("using for loop")

for i in range(1,11):
    print(f"{x} x {i} = {x*i}")

print("using while loop")

i = 1
while i < 11:
    print(f"{x} x {i} = {x*i}")
    i +=1


print("Reverse: ")

for i in range(10):
    print(f"{x} x {10-i} = {x*(10-i)}")