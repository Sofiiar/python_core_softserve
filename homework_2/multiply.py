#  Write a function that will receive 2 numbers as input and it should return the multiplication of these 2 numbers.


def mult_two(arg1, arg2):
    if not isinstance(arg1, (int, float)) or not isinstance(arg2, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return arg1 * arg2
