marks = {
    "Key":"Value",
    "Vivek" : 92,
    "Harsh" : 99,
    "Arish" : 79,
    "list":[1,2,3] 
}

print(marks, type(marks))

print(marks["Vivek"]) #returns error if doesn't exist
print(f"{marks.get("Vivek")}\n")  #returns none if doesn't exist
print(f"{marks["list"]}\n")

#metohs

print(f"{marks.items()}\n")
print(f"{marks.keys()}\n")
print(f"{marks.values()}\n")

marks.update({"Vivek":99})
marks.update({"Tejal":100})

student = {'name': 'Vivek', 'age': 20, 'marks': 88}

# Accessing
print(student.get('age'))        # 20
print(student.get('grade', 'N/A'))  # 'N/A' if not found

# Iterating
for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for k, v in student.items():
    print(f"{k}: {v}")

# Adding/updating
student.update({'grade': 'A'})
student['marks'] = 90

# Removing
student.pop('age')      # Removes 'age'
student.popitem()       # Removes last item (e.g., 'grade')

# Copying
student_copy = student.copy()


