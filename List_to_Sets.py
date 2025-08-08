list1 = []
list2 = []

# for i in range(1,5):
#     x = int(input(f"Enter number {i} for List 1: "))
#     list1.append(x)
    
# for i in range(1,5):
#     y = int(input(f"Enter number {i} for List 2: "))
#     list2.append(y)

list1 = list(map(int, input("Enter numbers for list 1 (space-separated): ").split()))

list2 = list(map(int, input("Enter numbers for list 2 (space-separated): ").split()))

#input("Enter numbers for list 2 (space-separated): ") --- input inst
#input as "1 2 3 4 5" as a string
# input().split()---split string by spaces ---['1', '2',...]--List os string
# map(int,['1','2',...])--- aplies int() to each element returns iterator
# list(map(...)) convert to list

set1 = set(list1)
set2 = set(list2)

print(f"\ncommon elements in both list are: {set1.intersection(set2)} ")
print(f"\nelements only in list 1 are: {set1.difference(set2)} ")
print(f"\nelements only in list 2 are: {set2.difference(set1)} ")
print(f"\nall elements of the lists are: {set2.union(set1)} ")
