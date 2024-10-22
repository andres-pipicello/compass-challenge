from main import Record, Comparison
from matching import email_matching


def test_equality():
    assert email_matching(Record(email="user@domain.com"), Record(email="user@domain.com")) == Comparison.MATCH
    assert email_matching(Record(email=""), Record(email="")) == Comparison.INCONCLUSIVE
    assert email_matching(Record(email="user@domain.com"), Record(email="other@domain.com")) == Comparison.NO_MATCH
    # Nulls are treated as missing data
    assert email_matching(Record(email="user@domain.com"), Record(email="")) == Comparison.INCONCLUSIVE
    assert email_matching(Record(email=""), Record(email="user@domain.com")) == Comparison.INCONCLUSIVE

def test_same_username():
    assert email_matching(Record(email="user@domain.com"), Record(email="user@alternative.com")) == Comparison.LIKELY
    assert email_matching(Record(email="user-suffix@domain.com"), Record(email="user@domain.com")) == Comparison.NO_MATCH
