import pytest
from homework_2.multiply import mult_two


@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (2, 3, 6),
        (2, 1, 2),
        (100, 100, 10000),
    ]
)
def test_multiply_valid(input_a, input_b, expected):
    assert mult_two(input_a, input_b) == expected


@pytest.mark.parametrize(
    "input_a, input_b",
    [
        ('a', 3),
        (2, None),
        (None, 'b'),
        ([1, 2], 3),
    ]
)
def test_multiply_invalid(input_a, input_b):
    with pytest.raises(TypeError):
        mult_two(input_a, input_b)