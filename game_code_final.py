import random

def get_difficulty():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty in ['easy', 'hard']:
            return difficulty
        print("Oops! Please type 'easy' or 'hard'.")

def get_guess():
    while True:
        try:
            guess = int(input("Take a wild guess: "))
            return guess
        except ValueError:
            print("That's not a number! Try again.")

def give_hint(guess, number):
    difference = guess - number
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

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("Think of a number between 1 and 100.")
    number = random.randint(1, 100)
    difficulty = get_difficulty()

    attempts = 10 if difficulty == 'easy' else 5
    print(f"You've chosen {difficulty} mode. You have {attempts} attempts to guess my number.")

    for attempt in range(attempts):
        guess = get_guess()
        hint = give_hint(guess, number)
        
        print(hint)
        
        if guess == number:
            break
        
        attempts_left = attempts - (attempt + 1)
        if attempts_left > 0:
            print(f"You have {attempts_left} attempts remaining.")
        else:
            print("Oh no! You've run out of attempts. Better luck next time!")

    print(f"The number was: {number}")

def main():
    while True:
        play_game()
        replay = input("Do you want to play again? Type 'yes' or 'no': ").lower()
        if replay != 'yes':
            break
    print("Thanks for playing! See you next time.")

if __name__ == "__main__":
    main()
