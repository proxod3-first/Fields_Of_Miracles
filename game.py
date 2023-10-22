import random


def choose_word():
    """
    Return a random word from the list of words.

    Returns:
        str: A randomly chosen word.
    """
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    return random.choice(words)


def display_word(word, guessed_letters):
    """
    Display the word with the guessed letters revealed.

    Args:
        word (str): The word to be displayed.
        guessed_letters (list): List of letters that have been guessed.

    Returns:
        str: The word with guessed letters revealed.
    """
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word


def play_game():
    """
    Play the game 'Field of Miracles'.

    The function chooses a random word to guess the letters of the word.
    It keeps track of the guessed letters and the number of tries.
    The function continues until the word is completely guessed or quitting.

    Returns:
        int: The number of tries it took to guess the word.
    """
    word = choose_word()
    guessed_letters = []
    tries = 0

    print("Welcome to the game 'Field of Miracles'!\n")
    print("The word contains", len(word), "letters.\n")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1:
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter. Try again.\n")
            continue

        guessed_letters.append(guess)
        tries += 1

        if guess not in word:
            print("The letter is not in the word.\n")
        else:
            print("Correct guess!\n")
        displayed_word = display_word(word, guessed_letters)
        print(displayed_word)

        if "_" not in displayed_word:
            print("Congratulations! You guessed the word in", tries, "tries.")
            break
    print("Thanks for playing!\n")
    return tries


play_game()
