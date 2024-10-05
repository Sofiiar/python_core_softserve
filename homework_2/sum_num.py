import re


def sum_num(txt):
    numbers = re.findall(r'\b\d+\b', txt)

    total_sum = sum(int(num) for num in numbers)
    return  total_sum
