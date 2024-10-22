from matching import first_name_matching, Record, Comparison


def test_equality():
    assert first_name_matching(Record(name="Robert"), Record(name="Robert")) == Comparison.MATCH
    assert first_name_matching(Record(name=""), Record(name="")) == Comparison.INCONCLUSIVE
    # Nulls are not treated nicely in names
    assert first_name_matching(Record(name="Richard"), Record(name="")) == Comparison.NO_MATCH
    assert first_name_matching(Record(name=""), Record(name="Richard")) == Comparison.NO_MATCH

def test_initials():
    assert first_name_matching(Record(name="Robert"), Record(name="R")) == Comparison.LIKELY
    assert first_name_matching(Record(name="Q"), Record(name="Quentin")) == Comparison.LIKELY
    assert first_name_matching(Record(name="Robert"), Record(name="Q")) == Comparison.NO_MATCH
    assert first_name_matching(Record(name="R"), Record(name="Quentin")) == Comparison.NO_MATCH
