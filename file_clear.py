with open("new_file.txt", "r") as f:
    text = f.read()
    print(text)

with open("new_file.txt", "w") as f:
    f.write("")

with open("new_file.txt", "r") as f:
    text = f.read()
    if text == "":
        print("No data in file.")