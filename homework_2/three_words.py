"""
You are given a string with words and numbers
separated by whitespaces (one space).
The words contains only letters.
You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end"
contains three words in succession.
"""


def three_words(txt):
    words = txt.split()
    count = 0

    for word in words:
        if word.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0

    return False


def three_words_sliding_window(txt):
    words = txt.split()

    for i in range(len(words) - 2):
        three_words_from_txt = words[i: i + 3]
        if all(word.isalpha() for word in three_words_from_txt):
            return True

        return False
