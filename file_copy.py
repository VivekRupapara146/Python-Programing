with open("this.txt", "r") as f :
    content = f.read()
    

with open("new_file.txt", "w") as g:
    g.write(content)
    
with open("new_file.txt", "r") as g:
    new_content = g.read()

if content == new_content:
    print(f"The text in files \'this.txt\' and \'new_file.txt\' is same")
else:print("The files have different content")

# also use input to give files and check from the given files