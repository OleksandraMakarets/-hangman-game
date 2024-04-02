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
