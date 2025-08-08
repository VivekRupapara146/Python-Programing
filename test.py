with open ("hiscore.txt", "r") as f:
        hiscore = f.read()
        print(hiscore , type(hiscore))
        h = int(hiscore)
        print(h , type(h))