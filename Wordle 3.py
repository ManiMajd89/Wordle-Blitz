print("Welcome to Wordle Blitz\n *****************************************************************************************")
print("You start the game by guessing a 5-letter word.")
print("If you get the final word within 6 guesses, you win, otherwise, you lose.")

import random

# ANSI escape codes for colors
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"

word_list = [
    "apple", "baker", "candy", "dance", "eager", "flame", "grape", "hatch", "image", "jolly",
    "knack", "lunch", "march", "noble", "ocean", "piano", "queen", "ranch", "shiny", "torch",
    "union", "vivid", "whale", "xenon", "yacht", "zebra", "abide", "brave", "charm", "dream",
    "eagle", "faint", "glory", "heart", "ideal", "joint", "kiosk", "lemon", "mirth", "nerve",
    "orbit", "pride", "quill", "reign", "skirt", "trend", "umbra", "vigor", "wrist", "xylus",
    "yield", "zesty", "acute", "blink", "crisp", "drove", "evoke", "flint", "gloat", "harsh",
    "itchy", "jazzy", "kneel", "lunar", "motel", "novel", "olive", "pixel", "quake", "rider",
    "smart", "tulip", "usher", "vixen", "wound", "xerox", "youth", "zonal", "aloft", "boast",
    "curve", "dizzy", "elbow", "frost", "glide", "hasty", "inbox", "jumpy", "kudos", "latch",
    "meant", "nylon", "omega", "punch", "quart", "risky", "siren", "taunt", "ultra", "vivid"
]
word = random.choice(word_list)

for i in range(6):
    guess = input("Guess a 5-letter word: ")

    while len(guess) != 5:
        print("The input is not 5 letters. Please enter a 5-letter word.")
        guess = input("Guess a 5-letter word: ")

    if guess == word:
        print(f"{RED}Congrats! You guessed the word correctly!{RESET}")
        break
    else:
        feedback = ""
        for j in range(5):
            if guess[j] == word[j]:
                feedback += f"{RED}{guess[j]}{RESET}"
            elif guess[j] in word:
                feedback += f"{YELLOW}{guess[j]}{RESET}"
            else:
                feedback += guess[j]
        print(feedback)

else:
    print(f"{RED}Game Over! The correct word was '{word}'.{RESET}")

print("Thanks for playing!")

else:
    print(f"{RED}Game Over! The correct word was '{word}'.{RESET}")

print("Thanks for playing!")
