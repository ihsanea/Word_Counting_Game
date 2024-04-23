# word_guessing_game.py

import random

class WordGuessingGame:
    def __init__(self, word_bank):
        self.word_bank = word_bank
        self.secret_word = random.choice(self.word_bank).lower()
        self.guessed_letters = []
        self.word_guesses = 0
        self.letter_guesses = 0
        self.max_word_guesses = 3

    def display_word_status(self):
        """
        Displays the word with guessed letters and underscores for unknown letters.
        """

        display = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display
    
    def guess_letter(self, letter):
        """
        Checks if the guessed letter is in the secret word.
        """
        self.letter_guesses += 1
        letter = letter.lower()
        if letter in self.secret_word:
            self.guessed_letters.append(letter)
            return f"Correct! '{letter} is in the word."
        else:
            return f"Sorry, '{letter}' is not in the word."
        
    def guess_word(self, word):
        """
        Checks if the guessed word is correct.
        """
        self.word_guesses += 1
        if word.lower() == self.secret_word:
            return f"Congratulations! You guessed the word '{word}' correctly in {self.letter_guesses} turns."
        else:
            return f"Sorry, '{word}' is not the correcct word."
        
# Example gameplay loop (You can expland this loop for multiple players)
while True:
    guess = input("Enter a letter or guess the word: ")
    if len(guess) == 1:
        print(game.guess_letter(guess))
        print("Current Word Status:", game.display_word_status())
    else:
        print(game.guess_word(guess))
        break
