
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

def write_csv(data):
    with open("calendar.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'short_name'])
        for row in data:
            writer.writerow([row['name'], row['short_name']])

@click.command()
def main():
    """Retrieve the names of the Discordian seasons to calendar.csv."""
    data = get_data()
    write_csv(data)

if __name__ == '__main__':
    main()

