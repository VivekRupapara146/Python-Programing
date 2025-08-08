student_marks = {}


for i in range(1,4):
    name = str(input(f"Enter name of student {i}: "))
    marks = int(input(f"Enter marks of the student {i}: ")) 
    student_marks[name] = marks   

print(student_marks)

for key, value in student_marks.items():
    print(f"Student name = {key}\tMarks = {value}")
    
topper = max(student_marks, key=student_marks.get)
print(f"\nTopper: {topper} with {student_marks[topper]} marks.")