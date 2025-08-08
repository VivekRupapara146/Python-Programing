#  Grading System with Conditional Expression

marks=int(input(f"Enter your marks"))
Grade =""

if 0<=marks<=100:
    if marks>=90: Grade = "A+"

    elif marks>=75: Grade = "A" 

    elif marks>=60: Grade = "B" 

    elif marks>=40: Grade = "C" 
    
    else: Grade= "Fail"
    
    print(f"Your grade is {Grade}") 

else:
    print("Invalid marks entered")

