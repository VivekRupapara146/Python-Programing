def add_student():
    name = input("Enter name of the student: ")
    try:
        maths = int(input("Enter marks in Maths: "))
        science = int(input("Enter marks in Science: "))
        english = int(input("Enter marks in English: "))
    except ValueError:
        print("Enter valid integral marks.")
        return
    
    with open ("Marks.txt", "a") as f:
        f.write(f"{name}, {maths}, {science}, {english}\n")
    
    print("Student added.\n")

def view_records():
    try:
        with open("Marks.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No records found.\n")
                return
        
            print("This is the the list of students and their marks in file: ")
            
            for l in lines:
                parts  = l.strip().split(",")
                name = parts[0]
                marks = list(map(int, parts[1:]))
                print(f"Name: {name}, Marks in [Science, Maths, English]: {marks}")
            print()
            
    except FileNotFoundError: 
        print("File not found.\n")
        
def main():
    while True:
        print("=====Student Marks Menu=====")
        print('''1. Add Student
2. View Data Inserted
3. Clear Data
4. Exit''')

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_records()
        elif choice == 3:
            with open("Marks.txt", "w") as f:
                f.write("")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.\n")

main()