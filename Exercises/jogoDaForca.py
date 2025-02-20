from wordslist import  words
import random

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}


def displayMan(wrongGuesses):
    for line in hangman_art[wrongGuesses]:
        print(line)


def displayHint(hint):
    print(" ".join(hint))


def displayAnswer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrongGuesses = 0
    guessedLetters = set()
    isRunning = True

    while isRunning:
        displayMan(wrongGuesses)
        displayHint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessedLetters:
            print(f"{guess} is already guessed")
            continue

        guessedLetters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrongGuesses += 1

        if "_" not in hint:
            displayMan(wrongGuesses)
            displayAnswer(answer)
            print("You Win!")
            isRunning = False
        elif wrongGuesses >= len(hangman_art) - 1:
            displayMan(wrongGuesses)
            displayAnswer(answer)
            print("You Lose!")
            isRunning = False


if __name__ == '__main__':
    main()