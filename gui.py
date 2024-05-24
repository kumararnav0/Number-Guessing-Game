import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 0
        
        self.create_widgets()

    def create_widgets(self):
        self.instructions = tk.Label(self.root, text="I'm thinking of a number between 1 to 100\nChoose a difficulty:")
        self.instructions.pack()

        self.easy_button = tk.Button(self.root, text="Easy", command=lambda: self.set_difficulty(10))
        self.easy_button.pack()

        self.hard_button = tk.Button(self.root, text="Hard", command=lambda: self.set_difficulty(5))
        self.hard_button.pack()

        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()
        self.guess_entry.config(state=tk.DISABLED)

        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess)
        self.guess_button.pack()
        self.guess_button.config(state=tk.DISABLED)
        
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def set_difficulty(self, max_attempts):
        self.max_attempts = max_attempts
        self.attempts = 0
        self.instructions.config(text=f"You have chosen {'Easy' if max_attempts == 10 else 'Hard'} difficulty.\nYou have {max_attempts} attempts to guess the number.")
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)
        self.result_label.config(text="")

    def make_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1

            if guess > self.number_to_guess:
                self.result_label.config(text="Number too high. Guess again.")
            elif guess < self.number_to_guess:
                self.result_label.config(text="Number too low. Guess again.")
            else:
                self.result_label.config(text="Congratulations! You guessed the right number!")
                messagebox.showinfo("Success", "Congratulations! You guessed the right number!")
                self.reset_game()
                return

            if self.attempts >= self.max_attempts:
                messagebox.showinfo("Game Over", f"Sorry, you've used all your attempts. The correct number was {self.number_to_guess}.")
                self.reset_game()
            else:
                self.result_label.config(text=f"{self.result_label.cget('text')}\nYou have {self.max_attempts - self.attempts} attempts remaining.")
                
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.DISABLED)
        self.instructions.config(text="I'm thinking of a number between 1 to 100\nChoose a difficulty:")
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
