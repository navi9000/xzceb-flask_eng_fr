'''Tests for translator'''

import unittest
from translator import english_to_french, french_to_english

class Tests(unittest.TestCase):
    '''Tests'''
    def test_english_to_french(self):
        '''English to French tests'''
        self.assertEqual(english_to_french(None), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english(self):
        '''French to English tests'''
        self.assertEqual(french_to_english(None), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
