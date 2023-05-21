
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

def create_longer_noun_filter(pattern, min_len, max_len):
    def longer_noun(entry):
        word, flags = entry
        if not re.search(f'[{pattern}]', flags):
            return False
        return min_len <= len(word) <= max_len
    return longer_noun

@click.command()
@click.argument("input", type=click.File("r",encoding="utf-8"))
@click.option('-o', '--output', type=click.File('w', lazy=False, encoding="utf-8"), default='-', help='Write to file instead of stdout.')
@click.option('--min-len', type=click.INT, default=5, help='Minimum characters for the word')
@click.option('--max-len', type=click.INT, default=8, help='Maximum characters for the word')
@click.option('--pattern', default='HP', help='Pattern for selected words')
def main(input, output, min_len, max_len, pattern):
    """Extracts noun words of specified length from ispell dictionary.
    Files this was designed to work with are from https://github.com/tvondra/ispell_czech
    """
    for entry in filter(create_longer_noun_filter(pattern, min_len, max_len), ispell_entries(input)):
        output.write(entry[0] + "\n")

if __name__ == '__main__':
    main()
