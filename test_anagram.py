
import unittest
from anagram import is_anagram

class TestAnagram(unittest.TestCase):
    def test_simple_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))

    def test_not_anagram(self):
        self.assertFalse(is_anagram("hello", "world"))

    def test_case_insensitive(self):
        self.assertTrue(is_anagram("Listen", "Silent"))

    def test_with_spaces(self):
        self.assertTrue(is_anagram("conversation", "voices rant on"))
