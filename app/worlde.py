import sys
import random

# each of our text files contains 1000 words
LISTSIZE = 1000

# values for colors and score (EXACT == right letter, right place; CLOSE == right letter, wrong place; WRONG == wrong letter)
EXACT = 2
CLOSE = 1
WRONG = 0

# ANSI color codes for boxed in letters
GREEN = "\033[38;2;255;255;255;1m\033[48;2;106;170;100;1m"
YELLOW = "\033[38;2;255;255;255;1m\033[48;2;201;180;88;1m"
RED = "\033[38;2;255;255;255;1m\033[48;2;220;20;60;1m"
RESET = "\033[0;39m"

# user-defined function prototypes
def get_guess(wordsize):
    guess = input(f"Input a {wordsize}-letter word:")
    if len(guess) == wordsize:
        return guess
    else:
        print(f"Invalid guess length. Please enter a {wordsize}-letter word.")
        return get_guess(wordsize)

def check_word(guess, wordsize, status, choice):
    for i in range(wordsize):
        if guess[i] == choice[i]:
            status[i] = EXACT
        elif guess[i] in choice:
            status[i] = CLOSE
        else:
            status[i] = WRONG
    return sum(status)

def print_word(guess, wordsize, status):
    for i in range(wordsize):
        if status[i] == EXACT:
            print(GREEN + guess[i] + RESET, end="")
        elif status[i] == CLOSE:
            print(YELLOW + guess[i] + RESET, end="")
        else:
            print(RED + guess[i] + RESET, end="")
    print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} wordsize")
        sys.exit(1)

    # ensure argv[1] is either 5, 6, 7, or 8 and store that value in wordsize instead
    wordsize = int(sys.argv[1])
    if wordsize not in [5, 6, 7, 8]:
        sys.exit(1)

    # open correct file, each file has exactly LISTSIZE words
    wl_filename = f"{wordsize}.txt"
    try:
        with open(wl_filename, "r") as wordlist:
            options = [word.strip() for word in wordlist.readlines()]
    except FileNotFoundError:
        print(f"Error opening file {wl_filename}.")
        sys.exit(1)

    # pseudorandomly select a word for this game
    choice = random.choice(options)

    # allow one more guess than the length of the word
    guesses = wordsize + 1
    won = False

    # print greeting, using ANSI color codes to demonstrate
    print(GREEN + "This is WORDLE50" + RESET)
    print(f"You have {guesses} tries to guess the {wordsize}-letter word I'm thinking of")

    # main game loop, one iteration for each guess
    for i in range(guesses):
        # obtain user's guess
      guess = get_guess(wordsize)

        # array to hold guess status, initially set to zero
      status = [WRONG] * wordsize

        # Calculate score for the guess
      score = check_word(guess, wordsize, status, choice)
