import doctest


def test_doctests():
    import memoized
    results = doctest.testmod(memoized)
    assert results.failed == 0, results
