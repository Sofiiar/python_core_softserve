"""
In a given text you need to sum the numbers
while excluding any digits that form part of a word.
The text consists of numbers, spaces and letters from the English alphabet.
"""
import re


def sum_num(txt):
    chunks = txt.split()
    total_sum = sum(int(chunk) for chunk in chunks if chunk.isdigit())

    return total_sum


def sum_num_regex(txt):
    numbers = re.findall(r'\b\d+\b', txt)
    total_sum = sum(int(num) for num in numbers)

    return total_sum
