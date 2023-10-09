import unittest
from game import choose_word, display_word


class TestGameFunctions(unittest.TestCase):
    def test_choose_word(self):
        words = ["apple", "banana", "cherry", "date", "wildberry"]
        chosen_word = choose_word()
        self.assertIn(chosen_word, words)
        
    def test_choose_word2(self):
        words = ["app"]
        chosen_word = choose_word()
        self.assertNotIn(chosen_word, words)
        
    def test_display_word(self):
        word = "apple"
        guessed_letters = ["a", "p"]
        displayed_word = display_word(word, guessed_letters)
        self.assertEqual(displayed_word, "app__")


if __name__ == '__main__':
    unittest.main()