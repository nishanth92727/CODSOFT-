import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock, Paper, Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.label = tk.Label(master, text="Choose rock, paper, or scissors:")
        self.label.pack()

        choices = ["rock", "paper", "scissors"]

        for choice in choices:
            button = tk.Button(master, text=choice, command=lambda c=choice: self.play_round(c))
            button.pack(side=tk.LEFT, padx=5)

        self.score_label = tk.Label(master, text="Your Score: 0 | Computer Score: 0")
        self.score_label.pack(pady=10)

        self.instructions_label = tk.Label(master, text="Instructions:\nClick on one of the buttons to make your choice.\nThe game will display the result in a pop-up window.\nThe score will be updated after each round.")
        self.instructions_label.pack(pady=10)

    def play_round(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])

        result = self.determine_winner(user_choice, computer_choice)

        messagebox.showinfo("Result", f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}")

        if "win" in result:
            self.user_score += 1
        elif "lose" in result:
            self.computer_score += 1

        self.update_score_label()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "You win!"
        else:
            return "You lose!"

    def update_score_label(self):
        self.score_label.config(text=f"Your Score: {self.user_score} | Computer Score: {self.computer_score}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
