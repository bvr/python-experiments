
# from https://death.andgravity.com/output

import csv
import time
import click

def get_data():
    # pretend some API calls happen here
    time.sleep(2)
    return [
        {"name": "Chaos", "short_name": "Chs"},
        {"name": "Discord", "short_name": "Dsc"},
        {"name": "Confusion", "short_name": "Cfn"},
        {"name": "Bureaucracy", "short_name": "Bcy"},
        {"name": "The Aftermath", "short_name": "Afm"},
    ]

def write_csv(data, file):
    writer = csv.writer(file)
    writer.writerow(['name', 'short_name'])
    for row in data:
        writer.writerow([row['name'], row['short_name']])

@click.command()
@click.option('-o', '--output', type=click.File('w', lazy=False), default='-')
def main(output):
    """Retrieve the names of the Discordian seasons."""
    data = get_data()
    # click.File doesn't have a newline argument
    output.reconfigure(newline='')
    write_csv(data, output)

if __name__ == '__main__':
    main()

