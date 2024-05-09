# Word Guessing Game

This is a simple yet interactive Word Guessing Game implemented in Python. The game challenges players to guess a secret word from a predefined word bank, enhancing their vocabulary and spelling skills.

## How to Run the Game

1. Clone the repository:
2. Navigate to the project directory:
3. Install required libraries:
4. Run the game:

## Game Rules

- **Guess the Secret Word**: Start by guessing letters to find clues about the secret word.
- **Letter Guesses**: The game informs you how many occurrences of each guessed letter are in the secret word.
- **Word Guesses**: Optionally, attempt to guess the whole word.
- **Turns**: Players take turns guessing letters; the game tracks the number of letter and word guesses each player makes.

## Additional Features

- **Random Word Selection**: Each game randomly selects a word from a predefined word bank.
- **Limited Guesses**: Players are allowed only a limited number of word guesses before the game ends.

## New Enhancements

- **Statistical Analysis**: After each game, the software performs a statistical analysis using the Pandas library to provide insights into gameplay, such as the average number of guesses per game.
- **Graphical Representation**: Utilizing the Matplotlib library, the game presents a bar graph showing the average number of letter guesses per win or loss, allowing players to visually assess their performance over time.

## Installation Requirements

This game requires Python and the installation of the following Python libraries:
- Pandas
- Matplotlib

Ensure these are installed on your system by running `pip install pandas matplotlib` before starting the game.

## Credits

This game was developed by Ihsane Abdeddaim as part of a university project in Python programming. 

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details.

