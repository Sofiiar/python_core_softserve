"""
Write a function that will receive 2 numbers as input and it should return the multiplication of these 2 numbers.
"""


def mult_two(arg1, arg2):
    both_numbers = isinstance(arg1, (int, float)) and isinstance(arg2, (int, float))

    if not both_numbers:
        raise TypeError("Both arguments must be numbers")

    return arg1 * arg2
