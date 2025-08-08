'''
open as a variable... f , a, b, c, etc
open --- open("filename.txt", "mode")
  .close()
r - read
w - write(overwrite)
a - append(update)
x - new file
b - binary mode
t - text mode (defaut)

'''

with open("this.txt", "r") as f:
  text = f.read()
  print(text)

with open("this.txt", "w") as f:
  f.write("New text added old removed.\nSecond line")

with open("this.txt", "r") as f:
  new_text = f.read()
  print(new_text)

with open("New.txt", "w") as  f:
  f.write("This is a new file.")

with open("New.txt") as f:
  text2 = f.read()
  print(text2)

lines = ["Apple\n", "Banana\n", "Mango\n"]
with open("fruits.txt", "w") as f:
    f.writelines(lines)

with open("Fruits.txt", "r") as f:
  for line in f:
    print(line)
    
with open("fruits.txt", "r") as f:
    for line in f:
        print(line.strip())  # removes \n
