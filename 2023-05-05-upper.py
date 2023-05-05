
import unicodedata

s = 'Příliš žluťoučký kůň úpěl ďábelské ódy'
print(s.upper())

# from https://stackoverflow.com/questions/20729827/compare-2-strings-without-considering-accents-in-python

normalized = unicodedata.normalize('NFKD', s.upper()).encode('ASCII', 'ignore')
if unicodedata.normalize('NFKD', 'PRILIS').encode('ASCII', 'ignore') in normalized:
    print('Found')
