
import unicodedata
import random

def get_words(input_file):
    with open(input_file, encoding='utf-8') as file:
        return [line.rstrip() for line in file]

def upper_ascii(s):
    return unicodedata.normalize('NFKD', s.upper()).encode('ASCII', 'ignore')

def play(word):
    to_guess = [(c,False) for c in word.upper()]
    print(to_guess)

def main():
    words = get_words('hangman-words.txt')
    play(random.choice(words))
    while input("Play Again? (Y/N) ").upper() == "Y":
        play(random.choice(words))

if __name__ == "__main__":
    main()
