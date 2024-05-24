from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        difficulty = request.form['difficulty']
        session['number_to_guess'] = random.randint(1, 100)
        session['attempts'] = 0
        session['max_attempts'] = 10 if difficulty == 'easy' else 5
        return redirect(url_for('guess'))
    return render_template('index.html')

@app.route('/guess', methods=['GET', 'POST'])
def guess():
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            session['attempts'] += 1

            if guess > session['number_to_guess']:
                message = "Number too high. Guess again."
            elif guess < session['number_to_guess']:
                message = "Number too low. Guess again."
            else:
                message = "Congratulations! You guessed the right number!"
                return render_template('guess.html', message=message, win=True)

            if session['attempts'] >= session['max_attempts']:
                message = f"Sorry, you've used all your attempts. The correct number was {session['number_to_guess']}."
                return render_template('guess.html', message=message, win=False)

            return render_template('guess.html', message=message)
        except ValueError:
            message = "Invalid input. Please enter a valid number."
            return render_template('guess.html', message=message)

    return render_template('guess.html')

if __name__ == "__main__":
    app.run(debug=True)
