"""Hangman game by Popov Andrey"""
import random

WORDS = ["python", "java", "javascript", "php", "ruby", "github"]


def main():
    """Main entry point."""

    while True:
        print("Type \"play\" to play the game, \"exit\" to quit: ", end='')

        try:
            command = input("> ")
            match command:
                case "play":
                    game()
                case "exit":
                    break
                case _:
                    print("Unknown command")
        except KeyboardInterrupt:
            print(" Exiting...")
            break

    print("Bye!")


def game():
    """Game entry point."""

    print("HANGMAN")

    chosen_word = random.choice(WORDS)

    entered_letters = set()
    attempts = 8
    while attempts > 0:
        print()

        hidden_word = ''.join(
            [l if l in entered_letters else '-' for l in chosen_word])

        print(hidden_word)

        if hidden_word == chosen_word:
            print("You guessed the word!")
            break

        print("Input a letter: ", end='')
        guess = input("> ")

        if len(guess) != 1:
            print("You should input a single letter.")
            continue
        if guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a lowercase English letter.")
            continue
        if guess in entered_letters:
            print("You've already guessed this letter.")
        elif guess not in chosen_word:
            print("That letter doesn't appear in the word.")
            attempts -= 1
        entered_letters.add(guess)

    if attempts == 0:
        print("You lost!")
    else:
        print("You survived!")


if __name__ == "__main__":
    main()
