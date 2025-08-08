with open("Poems.txt", "r") as f:
    line = f.read()
    

list_1 = ["bad word 2", "bad word 3" , "bad words"]

for word in list_1:
    line = line.replace(word , "#" * len(word))
    line = line.replace(word.title() , "#" * len(word))
    line = line.replace(word.upper() , "#" * len(word))
        

with open("Poems.txt", "w") as g:
    g.write(line)