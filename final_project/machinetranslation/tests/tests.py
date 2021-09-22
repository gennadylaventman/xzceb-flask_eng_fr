import unittest
from ..translator import englishToFrench, frenchToEnglish

class TestLanguageTransaltion(unittest.TestCase):

    def test_englishToFrench_None(self):
        self.assertEqual(englishToFrench(None), None)

    def test_englishToFrench_Equal(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_englishToFrench_NotEqual(self):
        self.assertNotEqual(englishToFrench('Bonjour'), 'Hello')
 
    def test_frenchToEnglish_None(self):
        self.assertEqual(frenchToEnglish(None), None)

    def test_frenchToEnglish_Equal(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

    def test_frenchToEnglish_NotEqual(self):
        self.assertNotEqual(frenchToEnglish('Hello'), 'Bonjour')


if __name__ == '__main__':
    unittest.main()