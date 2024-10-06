import pytest
from homework_2.three_words import three_words, three_words_sliding_window


def test_three_words():
    assert three_words("Hello World hello") == True
    assert three_words("He is 123 man") == False
    assert three_words("1 2 3 4") == False
    assert three_words("bla bla bla bla") == True


def test_three_words_sliding_window():
    assert three_words_sliding_window("Hello World hello") == True
    assert three_words_sliding_window("He is 123 man") == False
    assert three_words_sliding_window("1 2 3 4") == False
    assert three_words_sliding_window("bla bla bla bla") == True
