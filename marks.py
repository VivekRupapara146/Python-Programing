marks = []

i=1
while i < 7:
    m = input(f"Enter marks of student {i}: ")
    marks.append(m)
    print(f"Marks of student {i} are {m}.")
    i+=1

marks.sort()
print(marks)
print(marks.pop(2))