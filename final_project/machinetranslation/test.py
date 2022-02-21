import unittest

from translator import english_to_french, french_to_english

class TestenglishtoFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french('NULL'), 'Hello World') # Test for null input for englishToFrench
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # Test for the translation of the world 'Hello' and 'Bonjour
 
        

class TestfrenchtoEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english('NULL'), 'Hello World') # Test for null input for frenchToEnglish
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # Test for the translation of the world 'Bonjour' and 'Hello'


unittest.main()