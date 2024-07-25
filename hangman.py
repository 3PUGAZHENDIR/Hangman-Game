import random

# Define categories with corresponding word lists
categories = {
    "Animals": ["elephant", "giraffe", "hippopotamus", "kangaroo", "alligator"],
    "Fruits": ["apple", "banana", "cherry", "mango", "pineapple"],
    "Countries": ["argentina", "brazil", "canada", "denmark", "egypt"]
}

# Hangman stages
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

def choose_word(category):
    return random.choice(categories[category])

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    print("Welcome to Hangman!")
    print("Choose a category:")
    for idx, category in enumerate(categories.keys(), 1):
        print(f"{idx}. {category}")

    category_choice = int(input("Enter the number of your choice: ")) - 1
    category = list(categories.keys())[category_choice]

    word = choose_word(category)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = len(hangman_stages) - 1

    print(f"\nYou chose the category: {category}")
    print(f"You can make up to {max_incorrect_guesses} incorrect guesses.")
    print("Let's begin!\n")

    while incorrect_guesses < max_incorrect_guesses:
        print(hangman_stages[incorrect_guesses])
        print(display_word(word, guessed_letters))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.\n")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(hangman_stages[incorrect_guesses])
        print(f"Sorry, you've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    hangman()
