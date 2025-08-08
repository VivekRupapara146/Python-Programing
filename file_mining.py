# Program to check if a log file contains the word 'python'
# find line number

def line_count(file):
    line_number = []
    with open (file, "r") as f:
        text = f.readlines()
        count = 0
        for lines in text:
            count += 1
            if "python" in lines.lower():
                line_number.append(count)
    print(f"The word \'python\' is found in the lines {line_number}.")

file_path = "logfile.txt"

with open (file_path, "r") as f:
    content = f.read().lower()
    if "python" in content:
        print(f"The file contains the word \"python\" in it.")
        line_count(file_path)
    else:
        print(f"The word \"python\" is not present in the file.")