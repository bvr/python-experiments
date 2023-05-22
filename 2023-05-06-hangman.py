
import unicodedata
import random
from rich.console import Console
from rich.panel import Panel

def get_words(input_file):
    with open(input_file, encoding='utf-8') as file:
        return [line.rstrip() for line in file]

def upper_ascii(s):
    return unicodedata.normalize('NFKD', s.upper()).encode('ASCII', 'ignore')

def show_entry(console, guess, num):
    console.clear()
    console.print(Panel(str(num) + ': ' + ' '.join([c if visible else '-'  for c,visible in guess]), expand=False, title='HANGMAN'))
    # TODO: Draw a hangman picture
    console.print()

def play(console, word):
    to_guess = [(c,False) for c in word.upper()]
    tries = []
    allowed_fails = 7
    while allowed_fails > 0:
        show_entry(console, to_guess, allowed_fails)
        if len(tries) > 0:
            console.print('Already tried: ' + ' '.join(tries))
        guess = console.input(f'Guess letter (? = help): ')
        
        if guess == '?':
            guess = random.choice([c for c, visible in to_guess if visible == False])

        visible_before = sum(visible for _,visible in to_guess)
        to_guess = [(c, visible or upper_ascii(guess) == upper_ascii(c)) for c,visible in to_guess]
        visible_after = sum(visible for _,visible in to_guess)

        if visible_after == len(to_guess):
            show_entry(console, to_guess, allowed_fails)
            print('You won')
            break

        if visible_after == visible_before:
            # TODO: prevent taking a mistake twice
            tries.append(guess)
            allowed_fails -= 1
    else:
        word = ' '.join([c for c,_ in to_guess])
        print(f'You lost, the word was {word}')

def main():
    words = get_words('hangman-words.txt')
    console = Console()

    while True:
        play(console, random.choice(words))
        if input("Play Again? (Y/N) ").upper() == "N":
            break

if __name__ == "__main__":
    main()
