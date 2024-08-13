import random

def choose_word():
    words = ["python", "java", "programming", "puzzle", "coding", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    print("Welcome to the Simple Puzzle Game!")

    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6
    score = 0

    current_display = display_word(word_to_guess, guessed_letters)
    print(f"\nCurrent word: {current_display}")

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid single letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter. Try again.")
    else:
        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts_left -= 1
            score -= 1
            print("Incorrect guess.")
        else:
            score += 1
            print("Correct guess!")

        if set(guessed_letters) == set(word_to_guess):
            print("\nCongratulations! You guessed the word:", word_to_guess)
        else:
            print(f"\nSorry, you ran out of attempts. The correct word was: {word_to_guess}")

    print(f"Your final score is: {score}")
    print("Thanks for playing the Simple Puzzle Game!")

if __name__ == "__main__":
    main()