import random

# Define categories and words for each category
categories = {
    "fruits": ["apple", "banana", "orange", "pear", "grape", "strawberry",
               "watermelon", "kiwi", "pineapple", "mango"],
    "animals": ["elephant", "giraffe", "zebra", "rhinoceros", "hippopotamus",
                "lion", "tiger", "monkey", "crocodile", "penguin"],
    "programming_languages": ["python", "java", "javascript", "ruby", "php",
                              "csharp", "html", "css", "sql", "swift"],
    "countries": ["usa", "ireland", "england", "luxembourg", "ukraine",
                  "brazil", "canada", "germany", "japan", "australia",
                  "france", "kazakhstan"],
    "cities": ["london", "paris", "manchester", "tokyo", "beijing", "kiyv",
               "cairo", "philadelphia", "sydney", "alexandria", "mumbai"],
    "colors": ["red", "blue", "pink", "yellow", "purple", "green", "orange",
               "black", "white", "lightgreen", "aquamarine"]
}


# Hangman logo and word "MAN" as ASCII art
def print_logo():
    logo = r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""

    man_text = r"""
  M   M   A   N   N
  MM MM  A A  NN  N
  M M M AAAAA N N N
  M   M A   A N  NN
"""
    print(logo)
    print(man_text)


# Function to choose a random word from a specific category and level
def choose_word(category, level):
    if category in categories:
        words = categories[category]
        easy_words = [word for word in words if len(word) <= 5]
        medium_words = [word for word in words if 6 <= len(word) <= 8]
        hard_words = [word for word in words if len(word) > 8]

        if level == "easy" and easy_words:
            return random.choice(easy_words)
        elif level == "medium" and medium_words:
            return random.choice(medium_words)
        elif level == "hard" and hard_words:
            return random.choice(hard_words)
        else:
            print("No words available for the selected level in this category")
            return None
    else:
        print("Invalid category.")
        return None


# Function to display hangman
def print_hangman(wrong):
    if wrong == 0:
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 1:
        print(r"""
+---+
O   |
    |
    |
   ===""")
    elif wrong == 2:
        print(r"""
+---+
O   |
|   |
    |
   ===""")
    elif wrong == 3:
        print(r"""
+---+
 O  |
/|  |
    |
   ===""")
    elif wrong == 4:
        print(r"""
+---+
 O  |
/|\ |
    |
   ===""")
    elif wrong == 5:
        print(r"""
+---+
 O  |
/|\ |
/   |
   ===""")
    else:
        print(r"""
+---+
 O  |
/|\ |
/ \ |
   ===""")


def play_hangman():
    print("Welcome to Hangman!")
    print_logo()  # Print hangman logo with the word "MAN"

    # Input validation for name
    while True:
        name = input("Enter your name: ")
        if name.strip():  # Check if name is not empty
            break
        else:
            print("Please enter a valid name.")

    print("Rules:")
    print("- You will be presented with a word to guess.")
    print("- Guess the letters in the word.")
    print("- You have 6 attempts to guess the word correctly.")
    print("- For each incorrect guess, a part of the hangman will be drawn.")
    print("- If you guess the word correctly, you win!")
    print("- If you use up all tries, the hangman is drawn fully, resulting "
          "in a loss.")
    print("- Good luck!")
    print("================================"
          "================================================")

    while True:
        # Input validation for category
        while True:
            print("Choose a category:")
            for i, category in enumerate(categories.keys(), start=1):
                print(f"{i}. {category.capitalize()}")
            category_choice = input("Enter the category number: ").strip()
            if (
                category_choice.isdigit() and
                1 <= int(category_choice) <= len(categories)
            ):
                category = list(categories.keys())[int(category_choice) - 1]
                break
            else:
                print("Invalid choice. Please enter a valid number.")

        # Input validation for level
        while True:
            print("================================"
                  "================================================")
            print("Choose a level:")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            level_choice = input("Enter the level number: ").strip()
            if level_choice.isdigit() and 1 <= int(level_choice) <= 3:
                levels = ["easy", "medium", "hard"]
                level = levels[int(level_choice) - 1]
                break
            else:
                print("Invalid choice. Please enter a valid number.")

        word = choose_word(category, level)
        if not word:
            return

        # Initialize variables
        guessed_letters = []  # List to store guessed letters
        incorrect_letters = []  # List to store incorrect letters
        tries = 6  # Number of allowed incorrect guesses
        guessed_word = ['_'] * len(word)  # List to track guessed characters

        # Main game loop
        while tries > 0 and '_' in guessed_word:
            # Display current progress
            print(" ".join(guessed_word))
            print("Incorrect letters: ", ", ".join(incorrect_letters))
            print_hangman(6 - tries)  # Display the hangman
            print(f"Tries left: {tries}")
            guess = input("Guess a letter: ").lower()

            # Validate the guess
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You've already guessed that letter.")
                continue

            # Check if the guessed letter is in the word
            guessed_letters.append(guess)

            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        guessed_word[i] = guess
                print("Correct!")
            else:
                tries -= 1
                incorrect_letters.append(guess)
                print("Incorrect!")

        # Game result
        if '_' not in guessed_word:
            print(f"Congratulations, {name}! You've guessed the word:", word)
        else:
            print("Game over, you lose! The word was:", word)
            print_hangman(6)  # Display the last hanged man when losing

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Thank you for playing, {name}! Have a nice day!")
            return


# Play the game
play_hangman()
