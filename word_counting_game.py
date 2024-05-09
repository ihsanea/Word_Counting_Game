import random  # Import the random module to select a random word from the word bank
import pandas as pd  # Import Pandas for data handling
import matplotlib.pyplot as plt  # Import Matplotlib for creating graphs

class WordGuessingGame:
    def __init__(self, word_bank):
        # Constructor initializes the game with a list of words provided
        self.word_bank = word_bank  # Stores the list of possible words
        self.secret_word = random.choice(self.word_bank).lower()  # Randomly select a word and convert it to lowercase
        self.guessed_letters = []  # List to keep track of letters guessed by the player
        self.word_guesses = 0  # Count of word guesses made by the player
        self.letter_guesses = 0  # Count of letter guesses made by the player
        self.max_word_guesses = 3  # Maximum allowed word guesses
        self.game_stats = []  # List to keep track of game statistics
        self.game_over = False  # Flag to indicate if the game has ended

    def display_word_status(self):
        # This method displays the current status of the word being guessed
        display = ""  # Initialize the display string
        for letter in self.secret_word:  # Loop through each letter in the secret word
            if letter in self.guessed_letters:  # If the letter has been guessed,
                display += letter + " "  # Add the letter and a space to the display
            else:
                display += "_ "  # Otherwise, add an underscore and a space to represent unguessed letters
        return display  # Return the constructed display string

    def guess_letter(self, letter):
        # Method for handling a letter guess
        self.letter_guesses += 1  # Increment the count of letter guesses
        letter = letter.lower()  # Convert the guessed letter to lowercase
        if letter in self.secret_word and letter not in self.guessed_letters:  # Check if the guessed letter is in the secret word
            self.guessed_letters.append(letter)  # If yes, add it to the guessed letters list
            return "Correct! '{}' is in the word.".format(letter)  # Return a positive response
        else:
            return "Sorry, '{}' is not in the word.".format(letter)  # Otherwise, return a negative response

    def guess_word(self, word):
        # Method for handling a word guess
        self.word_guesses += 1  # Increment the count of word guesses
        if word.lower() == self.secret_word:  # Compare the guessed word (in lowercase) to the secret word
            self.end_game(True)  # End the game with a win
            return "Congratulations! You guessed the word '{}' correctly in {} turns.".format(word, self.letter_guesses)
        else:
            if self.word_guesses >= self.max_word_guesses:  # Check if the maximum number of word guesses has been reached
                self.end_game(False)  # End the game with a loss
            return "Sorry, '{}' is not the correct word.".format(word)  # If incorrect, inform the player

    def end_game(self, win):
        # Record game statistics and end the game
        self.game_stats.append({
            'letter_guesses': self.letter_guesses,
            'word_guesses': self.word_guesses,
            'result': 'Win' if win else 'Loss'
        })
        if win or self.word_guesses >= self.max_word_guesses:
            self.game_over = True  # Set the game over flag
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
while not game.game_over:  # Continue the game until the game_over flag is True
    guess = input("Enter a letter or guess the word: ")
    if len(guess) == 1:
        print(game.guess_letter(guess))
        print("Current Word Status:", game.display_word_status())
    else:
        print(game.guess_word(guess))
        if game.game_over:  # Check if the game should end
            break