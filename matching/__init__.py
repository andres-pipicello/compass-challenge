from dataclasses import dataclass
from enum import IntEnum


@dataclass
class Record:
    contactID: str = None
    name: str = None
    name1: str = None
    email: str = None
    postalZip: str = None
    address: str = None


class Comparison(IntEnum):
    MATCH = 1
    LIKELY = 2
    INCONCLUSIVE = 3
    NO_MATCH = 4


def name_matching(first: str, second: str) -> Comparison:
    first = first.lower()
    second = second.lower()
    if first == second:
        if not first:
            # both null
            return Comparison.INCONCLUSIVE
        if len(first) == 1:
            # both are initials
            return Comparison.LIKELY
        return Comparison.MATCH
    if not first or not second:
        return Comparison.NO_MATCH
    if first[0] == second[0] and (len(first) == 1 or len(second) == 1):
        # same first letter and one of them is an initial
        return Comparison.LIKELY
    return Comparison.NO_MATCH


def first_name_matching(first: Record, second: Record) -> Comparison:
    return name_matching(first.name, second.name)


def last_name_matching(first: Record, second: Record) -> Comparison:
    return name_matching(first.name1, second.name1)


def loose_equality(first, second) -> Comparison:
    if first == second:
        if not first:
            # both null
            return Comparison.INCONCLUSIVE
        return Comparison.MATCH
    if not first or not second:
        # Missing data is treated as INCONCLUSIVE
        return Comparison.INCONCLUSIVE
    return Comparison.NO_MATCH


def email_matching(first: Record, second: Record) -> Comparison:
    as_loose_equality = loose_equality(first.email, second.email)
    if as_loose_equality != Comparison.NO_MATCH:
        return as_loose_equality
    first_user, _ = first.email.split('@')
    second_user, _ = second.email.split('@')
    if first_user == second_user:
        return Comparison.LIKELY
    return Comparison.NO_MATCH


def zip_matching(first: Record, second: Record) -> Comparison:
    return loose_equality(first.postalZip, second.postalZip)


ADDRESS_COMPONENTS_VARIANTS = {
    'avenue': {'ave', 'av'},
    'street': {'st'},
    'road': {'rd'},
}

ADDRESS_COMPONENTS_LOOKUP = {
    variant: canonical
    for canonical, variants in ADDRESS_COMPONENTS_VARIANTS.items()
    for variant in variants
}


def address_matching(first: Record, second: Record) -> Comparison:
    return loose_equality(standardize_address(first.address), standardize_address(second.address))


def standardize_address(first_address):
    return " ".join(
        ADDRESS_COMPONENTS_LOOKUP.get(component) or component for component in
        first_address.lower().replace(".", "").replace(",", "").split(" ")
    )
