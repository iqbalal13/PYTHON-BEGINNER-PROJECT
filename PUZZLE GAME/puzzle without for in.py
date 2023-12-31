import random

def choose_word():
    words = ["python", "java", "programming", "puzzle", "coding", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    index = 0
    word_length = len(word)

    while index < word_length:
        letter = word[index]

        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

        index += 1

    return display

def main():
    print("Welcome to the Simple Puzzle Game!")

    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6

    while attempts_left > 0:
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"\nCurrent word: {current_display}")
        print(f"Attempts left: {attempts_left}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts_left -= 1
            print("Incorrect guess. Try again.")
        else:
            print("Correct guess!")

        if set(guessed_letters) == set(word_to_guess):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break

    if attempts_left == 0:
        print("\nSorry, you ran out of attempts. The correct word was:", word_to_guess)

    print("Thanks for playing the Simple Puzzle Game!")

if __name__ == "__main__":
    main()