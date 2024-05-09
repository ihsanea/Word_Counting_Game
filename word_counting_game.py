import random  # Import the random module to select a random word from the word bank
import pandas as pd
import matplotlib.pyplot as plt

class WordGuessingGame:
    def __init__(self, word_bank):
        self.word_bank = word_bank  # Stores the list of possible words
        self.secret_word = random.choice(self.word_bank).lower()  # Randomly select and convert to lowercase
        self.guessed_letters = []  # Track letters guessed by the player
        self.word_guesses = 0  # Count of word guesses made by the player
        self.letter_guesses = 0  # Count of letter guesses made by the player
        self.max_word_guesses = 3  # Maximum allowed word guesses
        self.game_stats = []  # Track stats for analysis

    def display_word_status(self):
        display = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display

    def guess_letter(self, letter):
        self.letter_guesses += 1
        letter = letter.lower()
        if letter in self.secret_word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            return "Correct! '{}' is in the word.".format(letter)
        else:
            return "Sorry, '{}' is not in the word.".format(letter)

    def guess_word(self, word):
        self.word_guesses += 1
        if word.lower() == self.secret_word:
            self.end_game(True)  # End the game with a win
            return "Congratulations! You guessed the word '{}' correctly in {} turns.".format(word, self.letter_guesses)
        else:
            if self.word_guesses >= self.max_word_guesses:
                self.end_game(False)  # End the game with a loss
            return "Sorry, '{}' is not the correct word.".format(word)

    def end_game(self, win):
        # Record game statistics
        self.game_stats.append({
            'letter_guesses': self.letter_guesses,
            'word_guesses': self.word_guesses,
            'result': 'Win' if win else 'Loss'
        })
        if win or self.word_guesses >= self.max_word_guesses:
            self.analyze_game_stats()  # Analyze and display game statistics

    def analyze_game_stats(self):
        # Use Pandas to analyze the game statistics
        df = pd.DataFrame(self.game_stats)
        print(df)
        df.groupby('result')['letter_guesses'].mean().plot(kind='bar', color=['green', 'red'])
        plt.title('Average Letter Guesses per Game Outcome')
        plt.xlabel('Game Outcome')
        plt.ylabel('Average Number of Guesses')
        plt.show()

# Define a list of words as the word bank
word_bank = ['apple', 'banana', 'cherry']

# Create an instance of the game with the word bank
game = WordGuessingGame(word_bank)

# Game loop to handle gameplay interactions
while True:
    guess = input("Enter a letter or guess the word: ")
    if len(guess) == 1:
        print(game.guess_letter(guess))
        print("Current Word Status:", game.display_word_status())
    else:
        print(game.guess_word(guess))
        if game.word_guesses >= game.max_word_guesses:
            break  # Exit the loop after the maximum number of word guesses