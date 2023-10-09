import random


def choose_word():
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    return random.choice(words)


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word


def play_game():
    word = choose_word()
    guessed_letters = []
    tries = 0

    print("Welcome to the game 'Field of Wonders'!")
    print("The word contains", len(word), "letters.")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1:
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter. Try again.")
            continue

        guessed_letters.append(guess)
        tries += 1

        if guess not in word:
            print("The letter is not in the word.")
        else:
            print("Correct guess!")
            
        displayed_word = display_word(word, guessed_letters)
        print(displayed_word)

        if "_" not in displayed_word:
            print("Congratulations! You guessed the word in", tries, "tries.")
            break
            