mport
unittest


class TestLenOperations(unittest.TestCase):

    def test_string_len(self):
        self.assertTrue(len("abc") > 0)

    def test_list_len(self):
        self.assertTrue(len([False, ]) > 0)

    def test_tuple_len(self):
        self.assertTrue(len([None, ]) > 0)

    def test_dict_len(self):
        self.assertTrue(len({"a": 123}) > 0)

    def test_set_len(self):
        self.assertTrue(len({1, "abc"}) > 0)
