from matching import Record, Comparison, zip_matching, address_matching


def test_equality():
    assert address_matching(Record(address="Ap #868-8966 Dolor. Street"),
                            Record(address="Ap #868-8966 Dolor. Street")) == Comparison.MATCH
    assert address_matching(Record(address="Ap #868-8966 Dolor. Street"),
                            Record(address="5545 Sed St.")) == Comparison.NO_MATCH

    # Missing Addresses codes are treated as missing data
    assert address_matching(Record(address=""), Record(address="")) == Comparison.INCONCLUSIVE
    assert address_matching(Record(address="Ap #868-8966 Dolor. Street"), Record(address="")) == Comparison.INCONCLUSIVE
    assert address_matching(Record(address=""), Record(address="Ap #868-8966 Dolor. Street")) == Comparison.INCONCLUSIVE


def test_abbreviations():
    assert address_matching(Record(address="Ap #868-8966 Dolor. Street"),
                            Record(address="Ap #868-8966 Dolor. St")) == Comparison.MATCH
    assert address_matching(Record(address="Ap #900-7243 Lorem. Avenue"),
                            Record(address="Ap #900-7243 Lorem. Ave")) == Comparison.MATCH
    assert address_matching(Record(address="3588 Mi Road"), Record(address="3588 Mi Rd.")) == Comparison.MATCH
