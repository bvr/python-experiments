
from unidecode import unidecode

s = 'Příliš žluťoučký kůň úpěl ďábelské ódy'
print(s.upper())

if unidecode('prilis'.upper()) in unidecode(s.upper()):
    print('Found')
