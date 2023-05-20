
import fileinput
from itertools import islice
import re
import click

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
    return 5 <= len(word) <= 8


@click.command()
@click.argument("input", type=click.File("r",encoding="utf-8"))
@click.option('-o', '--output', type=click.File('w', lazy=False, encoding="utf-8"), default='-', help='Write to file instead of stdout.')
def main(input, output):
    """Extracts noun words of specified length from ispell dictionary.
    Files this was designed to work with are from https://github.com/tvondra/ispell_czech
    """
    for entry in filter(longer_noun, ispell_entries(input)):
        output.write(entry[0] + "\n")

if __name__ == '__main__':
    main()
