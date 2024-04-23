import random  # Import the random module to select a random word from the word bank

class WordGuessingGame:
    def __init__(self, word_bank):
        # Constructor initializes the game with a list of words provided.
        self.word_bank = word_bank  # Stores the list of possible words.
        self.secret_word = random.choice(self.word_bank).lower()  # Randomly selects a word and converts it to lowercase.
        self.guessed_letters = []  # List to keep track of letters guessed by the player.
        self.word_guesses = 0  # Count of word guesses made by the player.
        self.letter_guesses = 0  # Count of letter guesses made by the player.
        self.max_word_guesses = 3  # Maximum allowed word guesses.

    def display_word_status(self):
        # This method displays the current status of the word being guessed.
        display = ""  # Initialize the display string.
        for letter in self.secret_word:  # Loop through each letter in the secret word.
            if letter in self.guessed_letters:  # If the letter has been guessed,
                display += letter + " "  # add the letter and a space to the display.
            else:
                display += "_ "  # Otherwise, add an underscore and a space to represent unguessed letters.
        return display  # Return the constructed display string.

    def guess_letter(self, letter):
        # Method for handling a letter guess.
        self.letter_guesses += 1  # Increment the count of letter guesses.
        letter = letter.lower()  # Convert the guessed letter to lowercase.
        if letter in self.secret_word:  # Check if the guessed letter is in the secret word.
            self.guessed_letters.append(letter)  # If yes, add it to the guessed letters list.
            return f"Correct! '{letter}' is in the word."  # Return a positive response.
        else:
            return f"Sorry, '{letter}' is not in the word."  # Otherwise, return a negative response.

    def guess_word(self, word):
        # Method for handling a word guess.
        self.word_guesses += 1  # Increment the count of word guesses.
        if word.lower() == self.secret_word:  # Compare the guessed word (in lowercase) to the secret word.
            return f"Congratulations! You guessed the word '{word}' correctly in {self.letter_guesses} turns."  # If correct, congratulate the player.
        else:
            return f"Sorry, '{word}' is not the correct word."  # If incorrect, inform the player.

# Define a list of words as the word bank.
word_bank = ['apple', 'banana', 'cherry']

# Create an instance of the game with the word bank.
game = WordGuessingGame(word_bank)

# Game loop to handle gameplay interactions.
while True:
    guess = input("Enter a letter or guess the word: ")  # Prompt the player to guess a letter or the word.
    if len(guess) == 1:  # Check if the input is a single letter.
        print(game.guess_letter(guess))  # Process the letter guess.
        print("Current Word Status:", game.display_word_status())  # Display the current status of the word.
    else:
        print(game.guess_word(guess))  # Process a word guess.
        break  # Exit the loop and end the game if a word guess is made.