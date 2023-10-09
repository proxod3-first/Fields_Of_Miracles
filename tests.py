import unittest
from game import display_word


class TestGameFunctions(unittest.TestCase):
    def test_display_word(self):
        word = "apple"
        guessed_letters = ["a", "p"]
        displayed_word = display_word(word, guessed_letters)
        self.assertEqual(displayed_word, "app__")


if __name__ == '__main__':
    unittest.main()