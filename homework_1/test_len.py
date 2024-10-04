def test_string_len():
    assert len("abc") > 0


def test_list_len():
    assert len([False]) > 0


def test_tuple_len():
    assert len([None]) > 0


def test_dict_len():
    assert len({"a": 123}) > 0


def test_set_len():
    assert len({1, "abc"}) > 0
