import random

WORDS = ["python", "computer", "programming", "developer", "internet"]
MAX_WRONG_GUESSES = 6


def display_word(word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def play_game():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("=" * 42)
    print("          CODEALPHA HANGMAN GAME")
    print("=" * 42)
    print("Guess the word one letter at a time.")
    print(f"You can make up to {MAX_WRONG_GUESSES} wrong guesses.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("Word:", display_word(word, guessed_letters))
        print("Guessed:", ", ".join(sorted(guessed_letters)) or "None")
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!\n")
        else:
            wrong_guesses += 1
            print("Incorrect guess!\n")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You won.")
            print(f"The word was: {word}")
            return

    print("Game over!")
    print(f"The correct word was: {word}")


if __name__ == "__main__":
    play_game()
