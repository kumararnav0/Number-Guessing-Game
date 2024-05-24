import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10
        
        self.create_widgets()
        self.set_difficulty("easy")

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Welcome to the Number Guessing Game!", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        
        self.instructions_label = tk.Label(self.root, text="Think of a number between 1 and 100.", font=("Helvetica", 12))
        self.instructions_label.pack(pady=5)
        
        self.difficulty_label = tk.Label(self.root, text="Choose a difficulty:", font=("Helvetica", 12))
        self.difficulty_label.pack(pady=5)
        
        self.easy_button = tk.Button(self.root, text="Easy", command=lambda: self.set_difficulty("easy"))
        self.easy_button.pack(pady=2)
        
        self.hard_button = tk.Button(self.root, text="Hard", command=lambda: self.set_difficulty("hard"))
        self.hard_button.pack(pady=2)
        
        self.guess_label = tk.Label(self.root, text="Take a wild guess:", font=("Helvetica", 12))
        self.guess_label.pack(pady=5)
        
        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.guess_entry.pack(pady=5)
        
        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=5)
        
        self.hint_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.hint_label.pack(pady=5)
        
        self.attempts_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.attempts_label.pack(pady=5)
        
        self.replay_button = tk.Button(self.root, text="Play Again", command=self.play_again)
        self.replay_button.pack(pady=5)
        self.replay_button.config(state=tk.DISABLED)
        
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.max_attempts = 10 if difficulty == "easy" else 5
        self.attempts = 0
        self.number = random.randint(1, 100)
        self.update_attempts_label()
        self.hint_label.config(text="")
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)
        self.replay_button.config(state=tk.DISABLED)

    def make_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.hint_label.config(text="That's not a number! Try again.")
            return

        self.attempts += 1
        hint = self.give_hint(guess)
        self.hint_label.config(text=hint)
        
        if guess == self.number or self.attempts >= self.max_attempts:
            self.guess_entry.config(state=tk.DISABLED)
            self.guess_button.config(state=tk.DISABLED)
            self.replay_button.config(state=tk.NORMAL)
        
        self.update_attempts_label()

    def give_hint(self, guess):
        difference = guess - self.number
        if difference == 0:
            return "Bingo! You guessed it right!"
        elif difference > 0:
            if difference > 20:
                return "Way too high! Aim lower."
            elif difference > 10:
                return "Too high! Try a lower number."
            elif difference > 5:
                return "A bit high. You're getting closer!"
            else:
                return "Very close, but just a tad high!"
        else:
            if difference < -20:
                return "Way too low! Aim higher."
            elif difference < -10:
                return "Too low! Try a higher number."
            elif difference < -5:
                return "A bit low. You're getting closer!"
            else:
                return "Very close, but just a tad low!"

    def update_attempts_label(self):
        attempts_left = self.max_attempts - self.attempts
        self.attempts_label.config(text=f"Attempts remaining: {attempts_left}")
        if self.attempts >= self.max_attempts and self.number != int(self.guess_entry.get()):
            self.hint_label.config(text=f"You've run out of attempts! The number was: {self.number}")
        
    def play_again(self):
        self.set_difficulty(self.difficulty)

def main():
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
