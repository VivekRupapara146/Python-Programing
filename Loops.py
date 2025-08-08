'''
reusability same code till a condition
eazy to get large block of code
1. While loop   2. For loop
while cond----->priority to check(looping time not known)
--body--(with cond to exit loop)

for item in iterable:(looping time known)
body
for - else:-- else executed at loop end
range(start, stop, skip_size)
break to exit loop continue to skip iteration
pass statement == null for loop body
'''
# i = 0
# while i<=50:
#     print(i)
#     i+=1

# num = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# i = 0
# while i<len(num):
#     print(num[i])
#     i += 1

# password
# i = 3
# while True and i>0:
#     password = input("Enter Password: ")
#     if password == "1234":
#         print("Access granted.")
#         break
#     else: 
#         print(f"Try again. Only {i-1} tries left.")
#         i -= 1