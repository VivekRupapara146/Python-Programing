# else-if single line

age = int(input(f"Enter your age: "))
status = "Adult" if age>=18 else "Minor"
print(f"\n{status}")

# if age >=18:
#     atatus = "Adult"
# else:
#     status = "Minor"

# elif ... chain of if else in py
# if cond1:
#     print
# elif cond2:
#     print
# else:
#     print

score = int(input(f"Enter your score: "))

# grade = "A" if score >= 90 else "B" if score >= 80 else "C"
# print(grade)

if score>=90:
    grade = "A"
elif score>=80:
    grade = "B"
else:
    grade = "C"

print(grade)