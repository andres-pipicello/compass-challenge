import csv
from dataclasses import dataclass


@dataclass
class Record:
    contactID: str
    name: str
    name1: str
    email: str
    postalZip: str
    address: str


def main():
    with open('input.csv', mode='r') as file:
        reader = csv.DictReader(file)
        records = [Record(**row) for row in reader]
        for record in records:
            print(record)


if __name__ == '__main__':
    main()
