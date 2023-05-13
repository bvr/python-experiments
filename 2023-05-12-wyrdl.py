# wyrdl.py
# from https://realpython.com/python-wordle-clone/
# based on https://www.nytimes.com/games/wordle/index.html

import pathlib
import random
from string import ascii_letters

def main():
    # Pre-process
    word = get_random_word()

    # Process (main loop)
    for guess_num in range(1, 7):
        guess = input(f"\nGuess {guess_num}: ").upper()

        show_guess(guess, word)
        if guess == word:
            print(f'wordS match')
            break
    # Post-process
    else:
        game_over(word)

def get_random_word():
    wordlist = pathlib.Path(__file__).parent / "wordlist.txt"
    words = [
        word.upper()
        for word in wordlist.read_text(encoding="utf-8").split("\n")
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)

def show_guess(guess, word):
    """Show the user's guess on the terminal and classify all letters.

    ## Example:

    >>> show_guess("CRANE", "SNAKE")
    Correct letters: A, E
    Misplaced letters: N
    Wrong letters: C, R
    """
    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))

def game_over(word):
    print(f"The word was {word}")

if __name__ == "__main__":
    main()
