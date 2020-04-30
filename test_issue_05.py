import unittest
from unittest.mock import patch
from issues import what_is_year_now
import urllib.request
import io


class TestTF(unittest.TestCase):

    def setUp(self):
        self.test_cases = {'{"currentDateTime":"2019-03-01"}',
                           '{"currentDateTime":"01.03.2019"}',
                           '{"currentDateTime":"2019.03.01"}',
                           '{"currentDataTime":"2019.03.01"}'}

    def tearDown(self):
        print('bye')

    def test_from_set(self):
        for case in self.test_cases:
            with patch('urllib.request.urlopen') as url_mock:
                url_mock.return_value.__enter__.return_value = io.StringIO(case)

                try:
                    what_is_year_now.what_is_year_now()
                except (ValueError, KeyError) as exception:
                    print('invalid format')
                    self.assertRaises(exception)
