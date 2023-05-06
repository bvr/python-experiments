
import unicodedata

def get_word():
    return "strom"

def upper_ascii(s):
    return unicodedata.normalize('NFKD', s.upper()).encode('ASCII', 'ignore')

def play(word):
    to_guess = [(c,False) for c in word.upper()]
    print(to_guess)

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
