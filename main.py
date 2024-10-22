import csv
from collections import Counter
from dataclasses import dataclass
from enum import IntEnum


class Comparison(IntEnum):
    MATCH = 1
    LIKELY = 2
    INCONCLUSIVE = 3
    NO_MATCH = 4


@dataclass
class Record:
    contactID: str
    name: str
    name1: str
    email: str
    postalZip: str
    address: str


def name_matching(first: str, second: str) -> Comparison:
    if first == second:
        if not first:
            return Comparison.INCONCLUSIVE
        if len(first) == 1:
            return Comparison.LIKELY
        return Comparison.MATCH
    if first[0] == second[0] and ((len(first) == 1) ^ (len(second) == 1)):
        return Comparison.LIKELY
    return Comparison.NO_MATCH


def first_name_matching(first: Record, second: Record) -> Comparison:
    return name_matching(first.name, second.name)


def last_name_matching(first: Record, second: Record) -> Comparison:
    return name_matching(first.name1, second.name1)


def email_matching(first: Record, second: Record) -> Comparison:
    if first.email == second.email:
        if not first.email:
            return Comparison.INCONCLUSIVE
        return Comparison.MATCH
    if not first.email or not second.email:
        return Comparison.NO_MATCH
    first_user, first_domain = first.email.split('@')
    second_user, second_domain = second.email.split('@')
    if first_user == second_user:
        return Comparison.LIKELY
    return Comparison.NO_MATCH


def zip_matching(first: Record, second: Record) -> Comparison:
    if first.postalZip == second.postalZip:
        if not first.postalZip:
            return Comparison.INCONCLUSIVE
        return Comparison.MATCH
    if not first.postalZip or not second.postalZip:
        return Comparison.NO_MATCH
    return Comparison.NO_MATCH


def address_matching(first: Record, second: Record) -> Comparison:
    if first.address == second.address:
        if not first.address:
            return Comparison.INCONCLUSIVE
        return Comparison.MATCH
    if not first.address or not second.address:
        return Comparison.INCONCLUSIVE
    return Comparison.NO_MATCH


def main():
    comparison_functions = [
        first_name_matching,
        last_name_matching,
        email_matching,
        zip_matching,
        address_matching
    ]

    with open('input.csv', mode='r') as file:
        reader = csv.DictReader(file)
        records = [Record(**row) for row in reader]
        for i in range(len(records)):
            for j in range(i + 1, len(records)):
                (first, second) = (records[i], records[j])
                comparison_results = {function: function(first, second) for function in comparison_functions}
                comparison_counters = Counter(comparison_results.values())
                if comparison_counters[Comparison.NO_MATCH] == 0:
                    nice_results = sorted((key.name, count) for key, count in comparison_counters.items())
                    print(f"Result: {nice_results} -> {first} and {second} match")


if __name__ == '__main__':
    main()
