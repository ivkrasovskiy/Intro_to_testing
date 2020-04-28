import unittest
from issues import one_hot_encoder as src


class TestTF(unittest.TestCase):
    def test_tf(self):
        actual = src.fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]

        self.assertEqual(actual, expected)

    def test_empty(self):
        actual = src.fit_transform([])
        expected = []
        self.assertEqual(actual, expected)

    def test_len(self):
        actual = src.fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertTrue(len(actual) == len(expected))

    def test_features_len(self):
        actual = len(set(['Moscow', 'New York', 'Moscow', 'London']))
        expected = len([
                           ('Moscow', [0, 0, 1]),
                           ('New York', [0, 1, 0]),
                           ('Moscow', [0, 0, 1]),
                           ('London', [1, 0, 0]),
                       ][0][1])
        self.assertEqual(actual, expected)

    def test_exceptions(self):
        actual = all(isinstance(city, str) for city in ['Moscow', 'New York', 'Moscow', 1])

        if actual:
            self.assertRaises(ValueError)


if __name__ == '__main__':
    unittest.main()
