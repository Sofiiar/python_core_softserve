def test_sorted_default():
    assert sorted(["banana", "ball", "cat"]) == ["ball", "banana", "cat"]


def test_sorted_by_length():
    assert sorted(["banana", "ball", "cat"], key=len) == ["cat", "ball", "banana"]


def test_sorted_reverse():
    assert sorted(["banana", "ball", "cat"], reverse=True) == ["cat", "banana", "ball"]


def test_sorted_reverse_by_length():
    assert sorted(["banana", "ball", "cat"], reverse=True, key=len) == ["banana", "ball", "cat"]
