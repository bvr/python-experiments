
import fileinput
from itertools import islice
import re

def ispell_entries(file):
    for line in file:
        # each line can contain multiple entries - "blána/Z blanou blan blanám blanách blanami"
        for entry in line.rstrip().split(' '):
            word, sep, flags = entry.partition('/')

            # handle format like {a,in,post,pre,su}fix
            match = re.search(r' \{ (?P<prefix> .*? ) \} (?P<rest> .* )$', word, re.VERBOSE)
            if match:
                for prefix in match.group('prefix').split(','):
                    yield prefix + match.group('rest'), flags
            else:
                yield word, flags

def longer_noun(entry):
    word, flags = entry
    if not re.search(r'[HP]', flags):
        return False
    return len(word) >= 8


# works on files from https://github.com/tvondra/ispell_czech
# if redirection into file is needed, the "set PYTHONIOENCODING=UTF-8" needs to be done
input = fileinput.input(encoding="utf-8")
for entry in filter(longer_noun, ispell_entries(input)):
    print(entry[0])
