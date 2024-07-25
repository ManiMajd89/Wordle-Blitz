print("Welcome to the Mani Wordle Game")
print("You start the game by guessing a 5-letter word.")
print("If you get the final word within 6 guesses, you win, otherwise, you lose.")

import random

# ANSI escape codes for colors
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"

word_list = ["apple", "table", "house", "mouse", "chair", "train", "knife", "tiger", "lemon", "melon", "piano", "radio", "cloud", "beach", "happy", "light", "money", "earth", "dream", "music", "quiet", "smile", "robot", "pilot", "heart", "storm", "wrist", "voice", "juice"]
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