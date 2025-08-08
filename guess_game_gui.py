import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime
import os

# Initialize game variables
n = random.randint(1, 100)
guesses = 0
highscore_file = 'highscore.txt'

# Read previous highscore (if any)
def get_highscore():
    if os.path.exists(highscore_file):
        with open(highscore_file, 'r') as f:
            lines = f.readlines()
            try:
                score = int(lines[0].strip())
                time = lines[1].strip()
                return score, time
            except:
                return None, ""
    return None, ""

# Save new highscore
def save_highscore(score):
    now = datetime.now()
    time = now.strftime("%d-%m-%Y %H:%M:%S")
    with open(highscore_file, 'w') as f:
        f.write(str(score) + "\n")
        f.write(f"Time of HighScore: {time}")

# Handle guess
def check_guess():
    global guesses
    try:
        user_guess = int(entry.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a number.")
        return

    guesses += 1
    if user_guess < n:
        feedback.set("Try a higher guess!")
    elif user_guess > n:
        feedback.set("Try a lower guess!")
    else:
        feedback.set(f"🎉 Correct! You guessed it in {guesses} tries.")
        old_score, _ = get_highscore()
        if old_score is None or guesses < old_score:
            save_highscore(guesses)
            messagebox.showinfo("New Highscore!", f"🏆 New highscore: {guesses} tries!")
        else:
            messagebox.showinfo("Game Over", f"You guessed correctly in {guesses} tries!")
        update_highscore()
        reset_game()

# Reset game
def reset_game():
    global n, guesses
    n = random.randint(1, 100)
    guesses = 0
    entry.delete(0, tk.END)
    feedback.set("New game started. Guess the number!")

# Update highscore label
def update_highscore():
    score, t = get_highscore()
    if score:
        highscore_text.set(f"Highscore: {score} tries\n{t}")
    else:
        highscore_text.set("No highscore yet.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("350x250")

tk.Label(root, text="🎯 Guess a number between 1 and 100", font=("Helvetica", 12)).pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 12))
entry.pack(pady=5)

tk.Button(root, text="Guess", command=check_guess).pack(pady=5)

feedback = tk.StringVar()
tk.Label(root, textvariable=feedback, font=("Helvetica", 10)).pack()

highscore_text = tk.StringVar()
tk.Label(root, textvariable=highscore_text, font=("Helvetica", 10), fg="green").pack(pady=10)

update_highscore()
feedback.set("Start guessing...")

root.mainloop()
