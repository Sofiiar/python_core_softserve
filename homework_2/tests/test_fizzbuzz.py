import pytest
from homework_2.fizzbuzz import fizz_buzz


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (15, "Fizz Buzz"),
        (9, "Fizz"),
        (10, "Buzz"),
        (4, "4")
    ]
)
def test_fizz_buzz_valid(input_value, expected_output):
    assert fizz_buzz(input_value) == expected_output


@pytest.mark.parametrize(
    "input_value",
    [
        -1,
        0,
        3.5,
        "15",
    ]
)
def test_fizz_buzz_invalid(input_value):
    with pytest.raises(ValueError):
        fizz_buzz(input_value)
