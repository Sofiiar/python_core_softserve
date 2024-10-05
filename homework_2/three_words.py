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
