import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Rock, Paper, Scissors")
        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_choice = None
        self.history = []  # Store the player's previous moves
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self.root, text="Rock, Paper, Scissors", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)

        # Buttons for user choice
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        for choice in self.choices:
            button = tk.Button(button_frame, text=choice, font=("Arial", 16),
                               command=lambda c=choice: self.play_round(c))
            button.pack(side=tk.LEFT, padx=10)

        # Display Result
        self.result_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.result_label.pack(pady=20)

        # Reset Button
        reset_button = tk.Button(self.root, text="Reset Game", font=("Arial", 14), command=self.reset_game)
        reset_button.pack(pady=10)

    def play_round(self, user_choice):
        self.user_choice = user_choice
        ai_choice = self.get_ai_choice()

        # Determine the winner
        result = self.determine_winner(user_choice, ai_choice)

        # Display result
        self.result_label.config(
            text=f"You chose: {user_choice}\nAI chose: {ai_choice}\nResult: {result}")

        # Update history
        self.history.append(user_choice)

    def get_ai_choice(self):
        """AI predicts the user's next move based on history."""
        if len(self.history) < 2:
            return random.choice(self.choices)  # Random for the first few rounds
        else:
            # Simple Markov Chain: Predict next move based on the most common previous move
            last_move = self.history[-1]
            predicted_next = {
                "Rock": "Paper",      # Rock is countered by Paper
                "Paper": "Scissors",  # Paper is countered by Scissors
                "Scissors": "Rock"    # Scissors is countered by Rock
            }
            return predicted_next[last_move]

    def determine_winner(self, user, ai):
        if user == ai:
            return "It's a Draw!"
        elif (user == "Rock" and ai == "Scissors") or \
             (user == "Paper" and ai == "Rock") or \
             (user == "Scissors" and ai == "Paper"):
            return "You Win!"
        else:
            return "AI Wins!"

    def reset_game(self):
        self.history = []
        self.result_label.config(text="")
        messagebox.showinfo("Game Reset", "Game has been reset. Start again!")

# Run the game

root = tk.Tk()
game = RockPaperScissors(root)
root.mainloop()
