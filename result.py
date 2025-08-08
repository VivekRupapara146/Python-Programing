# # Write a program to find out whether a student
# is pass ror fail if it requires total 40% and
# at least 33%, in each subject to pass and take marks as an input from the user


max_marks = int(input("\nEnter maximum marks in a suject: "))
max_subject = int(input("\nEnter total number subject: "))
max_students = int(input("\nEnter total number students: "))
# mark_list = []
# perc_list = []

total_max = max_subject * max_marks

for s in range(1, max_students+1):
    print(f"\nStudent {s}")
    name = input("\nEnter student name: ")
    mark_list = []
    perc_list = []
    
    for i in range(1, max_subject+1):
        while True:
            marks = int(input(f"Enter marks of subject {i}: "))
            if 0<=marks<=max_marks:
                perc_list.append((marks/max_marks)*100)
                mark_list.append(marks)
                break
            else: 
                print("\nInvalid marks. Try again.")

    print(f"\nGiven marks are: {mark_list}")

    percentage = (sum(mark_list)/total_max)*100
    min_sub_percentage = min(perc_list)

    result = (
    "PASS" if percentage>=40 and min_sub_percentage>=33 else
    "FAIL" 
    )
    
    print("Note: Criteria for passing is overall 40% and above with 33% and above in all subjects")

    print(f'''
\nResult for {name}:\n
Marks: {mark_list}\n
Percentage: {percentage:.2f}%\n
Minimum subject %: {min_sub_percentage:.2f}%\n
FINAL RESULT: {result}
''')
