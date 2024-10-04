def test_divmod():
    assert divmod(5, 2) == (2, 1)


def test_power():
    assert pow(5, 2) == 25


def test_round():
    assert round(4.345, 2) == 4.34
    assert round(4.345) == 4
    assert round(4.345, 1) == 4.3


def test_sum():
    assert sum([1, 2, 3]) == 6
    assert sum((1, 2, 3)) == 6
    assert sum({1, 2, 3}) == 6