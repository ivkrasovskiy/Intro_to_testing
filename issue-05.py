from unittest import TestCase
from unittest.mock import patch
from issues import what_is_year_now
import urllib.request.urlopen


def side_effect_function(self, case):
    return case


def mock_simple_function_with_side_effect(mock_simple_func):
    mock_simple_func.side_effect = side_effect_function


class TestTF(TestCase):

    def setUp(self):
        self.test_cases = {'2019-03-01', '01.03.2019', '01-03-2019'}

    def tearDown(self):
        print('hi')

    def test_from_set(self):
        for case in self.test_cases:
            patch
            return_value = case
            what_is_year_now.what_is_year_now()
