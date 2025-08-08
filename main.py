# wwe are going to write a program that generates a random number and asks user to guess it.
# If the player guess is higher than the actual number., the program displays "Lower number please". Similaarly if the user's guess is higher it prints "Higher guess please"
# whenthe user guesses the correct number the program displays the number of guesses user took to arive at the number

import random
from datetime import datetime
now = datetime.now()
time = now.strftime("%d-%m-%Y %H:%M:%S")

n = random.randint(1, 100)
a = -1
guesses = 0
while a !=n:
  guesses += 1
  a = int(input("Guess the number: "))
  if a<n: 
    print("Try a higher guess!")
    continue
  elif a>n:
    print("Try a lower guess!")
  else: 
    break
print(f"You have guessed the number {a} in {guesses} tries.")

with open('highscore.txt', 'r') as f:
  o_highscore = int(f.readline())

if o_highscore >= guesses:
  print("You have scored highscore!")
  with open('highscore.txt', 'w') as f:
    f.write(str(guesses))
    f.write(f"\nTime of HighScore: {time}")
else:
  print(f"Your score is {guesses}")

with open('highscore.txt', 'r') as f:
  highscore = int(f.readline())
  t = f.readline()
print(f"HighScore is: {highscore}")
print(t)