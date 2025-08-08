name = input("Enter you name: ")

n = len(name)

if n >= 10: print("Name has mor than 10 characters")
else: print("Name has less than 10 characters")

name_list = ["Vivek", "Rahul", "Aryan", "Lalit"]

name2 = input("Enter name of your friend: ")

if name2 in name_list: print("Your friend's name is in the list.")
else:
    print("Your friend's name is not on the list but is added now.")
    name_list.append(name2)
