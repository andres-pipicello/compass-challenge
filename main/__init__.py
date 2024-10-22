import csv
from collections import Counter

from matching import first_name_matching, Record, Comparison, last_name_matching, email_matching, zip_matching, \
    address_matching


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
                if comparison_counters[Comparison.NO_MATCH] == 1:
                    nice_results = sorted((key.name, count) for key, count in comparison_counters.items())
                    print(f"Result: {nice_results} -> {first} and {second} match")
