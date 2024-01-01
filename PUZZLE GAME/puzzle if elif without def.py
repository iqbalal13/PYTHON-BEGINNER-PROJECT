import random

print("Welcome to the Simple Puzzle Game!")

words = ["python", "java", "programming", "puzzle", "coding", "computer"]
word_to_guess = random.choice(words)
guessed_letters = []
attempts_left = 6
score = 0

current_display = "".join([letter if letter in guessed_letters else "_" for letter in word_to_guess])
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