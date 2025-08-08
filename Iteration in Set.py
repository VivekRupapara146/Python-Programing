set = set()

for i in range(1,6):
    x = int(input(f"Enter unique number {i}: "))
    if x in set:
        print("Element alrweady exist! Enter different number")
    else:
        set.add(x)
    
for items in set:
    print(items)
    
print(f"Total length of set is {len(set)}")

y = int(input(f"\nEnter number you want to check for in the set: "))
if y in set:
    print(f"\n{y} is present in set")
else:
    print(f"\n{y} is not present in set")