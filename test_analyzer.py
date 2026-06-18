import unittest
from password_analyzer import analyze_password_strength

class TestPasswordAnalyzer(unittest.TestCase):

    def test_short_password(self):
        strength, feedback = analyze_password_strength("short")
        self.assertIn("Very Weak", strength)
        self.assertTrue(any("too short" in f for f in feedback))

    def test_repeated_characters(self):
        strength, feedback = analyze_password_strength("aaa123XYZ!")
        self.assertTrue(any("repeated characters" in f for f in feedback))

    def test_strong_password(self):
        strength, feedback = analyze_password_strength("Str0ng!P@ssw0rd")
        self.assertIn("Very Strong", strength)
        self.assertTrue(any("length is excellent" in f for f in feedback))

    def test_dictionary_word(self):
        strength, feedback = analyze_password_strength("apple")
        self.assertTrue(any("dictionary" in f for f in feedback))

if __name__ == '__main__':
    unittest.main()
