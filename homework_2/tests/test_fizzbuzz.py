import pytest
from homework_2.fizzbuzz import fizz_buzz


def test_fizz_buz():
    assert fizz_buzz(15) == "Fizz Buzz"
    assert fizz_buzz(9) == "Fizz"
    assert fizz_buzz(10) == "Buzz"
    assert fizz_buzz(4) == "4"

    with pytest.raises(ValueError):
        fizz_buzz(-1)

    with pytest.raises(ValueError):
        fizz_buzz(0)

    with pytest.raises(ValueError):
        fizz_buzz(3.5)

    with pytest.raises(ValueError):
        fizz_buzz("15")
