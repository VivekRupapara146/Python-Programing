'''
computer chooses then you choose
get its values 
compare with computer and run if else ladder

1 -- snake
0 -- water
-1 --gun
'''

import random
import datetime

def game():
    with open("hiscore.txt", "r") as h:
        h_score = h.read()
        print(f"Your previous highscore is: {h_score}")
    score = 0
    while True:
        youDict = {
            "s" : 1, "w" : 0 , "g" : -1
        }
        revDict = {
            -1 : "Gun", 0 : "Water", 1 : "Snake"
        }
        
        computer = random.choice([-1, 0, 1])
        print('''Score rules:
1. If you win you get +1 score.
2. If you lose your score gets zero
3. If draw, no update in score
4. Highscore will be saved.''')
                
        youstr =input("\nEnter your choise:\ns for 'snake', w for 'water or g for 'gun'\n").lower()
        if youstr not in youDict:
            print("Invalid input. Try again")
            continue
        
        you = youDict[youstr]

        print(f"You chose {revDict[you]}\nComputer chose {revDict[computer]}")
        
        if(computer == you):
            print("Its a DRAW.")
        elif (you == 1 and computer == 0 ) or (you == 0 and computer == -1 ) or (you == -1 and computer == 1 ):
            print("🎉 You WIN!")
            score += 1
            with open ("hiscore.txt", "r") as f:
                hiscore = f.read()
                if hiscore == "": hiscore_val = 0
                else: 
                    num_part = hiscore.split(",")[0].strip()
                    hiscore_val = int(num_part)
                if score > int(hiscore_val):
                    with open("hiscore.txt", "w") as g:
                        now = datetime.datetime.now()
                        g.write(f"{str(score)}, {now}")
                        print(f"You just made a hghscore of {score}")
                else:       
                    print(f"Your score is {score}")
        else: 
            print("😞 You LOSE!")
            score = 0
            print("Your score reset to zero(0).")
        
        c = input("\nDo you wanna play again? (y/n): ").lower()
        if c == "n":
            print("Thanks for playing! 👋")
            break
        elif c == "y":
            continue
        else: print("Invalid input but considered yes so play! 😈")

now = datetime.datetime.now()
game()
