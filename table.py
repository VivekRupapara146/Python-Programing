print("generating tables from 2 to 20 in a folder")

for i in range(2, 21):
    str = ""
    for j in range(10):
        str = str + (f"{i} * {j+1} = {i*(j+1)}\n")
    with open(f"D:\\Python\\Chapter 9 PS\\Tables\\Table_of_{i}.txt", "w") as f:
        f.write(str)