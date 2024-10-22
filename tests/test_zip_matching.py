from matching import Record, Comparison, zip_matching


def test_equality():
    assert zip_matching(Record(postalZip="90210"), Record(postalZip="90210")) == Comparison.MATCH
    assert zip_matching(Record(postalZip="90210"), Record(postalZip="33162")) == Comparison.NO_MATCH

    # Missing Zip codes are treated as missing data
    assert zip_matching(Record(postalZip=""), Record(postalZip="")) == Comparison.INCONCLUSIVE
    assert zip_matching(Record(postalZip="90210"), Record(postalZip="")) == Comparison.INCONCLUSIVE
    assert zip_matching(Record(postalZip=""), Record(postalZip="90210")) == Comparison.INCONCLUSIVE
