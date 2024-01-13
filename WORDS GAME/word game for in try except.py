import random

def choose_word():
    words = ["python", "programming", "game", "code", "challenge", "fun", "learning", "puzzle"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def random_words_game():
    print("Welcome to the Random Words Game!")
    secret_word = choose_word()
    guessed_letters = []
    max_attempts = 6

    for attempts in range(1, max_attempts + 1):
        print("\nCurrent word: ", display_word(secret_word, guessed_letters))
        print("Guessed letters: ", guessed_letters)
        
        try:
            guess = input("Guess a letter: ").lower()

            if not guess.isalpha() or len(guess) != 1:
                raise ValueError("Invalid input. Please enter a single letter.")
            
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            else:
                guessed_letters.append(guess)

                if guess not in secret_word:
                    print("Incorrect guess!")
                    print("Attempts remaining: ", max_attempts - attempts)
                else:
                    print("Good guess!")

                    if set(guessed_letters) >= set(secret_word):
                        print("Congratulations! You guessed the word:", secret_word)
                        break

        except ValueError as ve:
            print(ve)

    else:
        print("Sorry, you ran out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    random_words_game()