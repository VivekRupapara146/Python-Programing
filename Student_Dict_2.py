Student_detail = {}


for i  in range(1,4):
    std_name = str(input(f"\nEntername of student {i}: "))
    age = int(input(f"Enter age of {std_name}: "))
    marks = int(input(f"Enter marks of {std_name}: "))
    detail = {
        "age": age,
        "marks": marks
    }
    Student_detail[std_name] = detail

# print(Student_detail)

for name, detail in Student_detail.items():
    print(f"\nStudent name: {name}")
    print(f"Age: {detail['age']}\tMarks: {detail['marks']}")
        
topper = max(Student_detail, key=lambda name : Student_detail[name]['marks'])
print(f"\nTopper: {topper} with {Student_detail[topper]['marks']} marks.")
