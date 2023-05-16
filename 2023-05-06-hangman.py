
import unicodedata
import random

def get_words(input_file):
    with open(input_file, encoding='utf-8') as file:
        return [line.rstrip() for line in file]

def upper_ascii(s):
    return unicodedata.normalize('NFKD', s.upper()).encode('ASCII', 'ignore')

def show_entry(guess, num):
    print(str(num) + ': ' + ' '.join([c if visible else '-'  for c,visible in guess]))


def play(word):
    to_guess = [(c,False) for c in word.upper()]
    for guess_num in range(1, 7):
        print(to_guess)
        show_entry(to_guess, guess_num)
        guess = upper_ascii(input("Guess letter: "))
        to_guess = [(c, visible or guess == upper_ascii(c)) for c,visible in to_guess]
    

def main():
    words = get_words('hangman-words.txt')
    play(random.choice(words))
    while input("Play Again? (Y/N) ").upper() == "Y":
        play(random.choice(words))

if __name__ == "__main__":
    main()
