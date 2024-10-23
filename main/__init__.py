import csv

from matching import first_name_matching, Record, Comparison, last_name_matching, email_matching, zip_matching, \
    address_matching

COMPARISON_SCORES = {
    Comparison.MATCH: 1,
    Comparison.LIKELY: 0.5,
    Comparison.INCONCLUSIVE: 0.0,
    Comparison.NO_MATCH: -0.5
}

# Completely arbitrary, but can be interpreted as "if the majority of the results are LIKELY o better", it is a match
MATCH_THRESHOLD = 0.25


def accuracy_for_score(score: float) -> str:
    if score < MATCH_THRESHOLD:
        return "Irrelevant"
    if MATCH_THRESHOLD <= score < 0.5:
        return "Low"
    if 0.5 <= score < 0.8:
        return "Medium"
    return "High"


def main():
    comparison_functions = [
        first_name_matching,
        last_name_matching,
        email_matching,
        zip_matching,
        address_matching
    ]

    with open('input.csv', mode='rt') as file:
        reader = csv.DictReader(file)
        records = [Record(**row) for row in reader]

    with open('output.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')

        for i in range(len(records)):
            for j in range(i + 1, len(records)):
                (first, second) = (records[i], records[j])
                comparison_results = [function(first, second) for function in comparison_functions]
                comparison_score = sum(COMPARISON_SCORES[result] for result in comparison_results) / len(comparison_functions)

                if comparison_score >= MATCH_THRESHOLD:
                    writer.writerow([first.contactID, second.contactID, accuracy_for_score(comparison_score)])