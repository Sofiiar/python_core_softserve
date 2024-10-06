import pytest
from homework_2.sum_num import sum_num, sum_num_regex


def test_sum_num():
    assert sum_num("hi") == 0
    assert sum_num("who is 1st here") == 0
    assert sum_num("my numbers is 2") == 2
    assert sum_num("bla bla bla between 1845 and 1910 year")== 3755


def test_sum_num_regex():
    assert sum_num_regex("hi") == 0
    assert sum_num_regex("who is 1st here") == 0
    assert sum_num_regex("my numbers is 2") == 2
    assert sum_num_regex("bla bla bla between 1845 and 1910 year")== 3755
