# Write a program to read the teat from a giveen file 'poems txt" and find out whether it Contian the word twinkle.

with open("Poems.txt", "r") as f:
    line = f.read()
    if "twinkle" not in line.lower():
        print("The word 'twinkle' is not present in the poem")
    else:
        print("The word 'twinke is present in the poem")