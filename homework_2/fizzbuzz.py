def fizz_buzz(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer")

    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)