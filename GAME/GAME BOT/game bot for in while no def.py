import random

print("Welcome to the Guessing Game!")
secret_number = random.randint(1, 100)
score = 0

outer_attempts = 0
while outer_attempts < 3:  # Limit the number of attempts to 3 for this example
    inner_attempts = 0
    while inner_attempts < 3:  # Limit the number of input attempts to 3 for this example
        try:
            user_input = input("Enter your guess (1-100), 'skip' to pass the question: ")

            if user_input.lower() == 'skip':
                print("Question skipped. Your score for this question is set to 0.")
                score = 0
                break
            elif user_input.isdigit():
                guess = int(user_input)
                if 1 <= guess <= 100:
                    break
                else:
                    print("Please enter a number between 1 and 100.")
            else:
                print("Invalid input. Please enter a valid number or 'skip'.")
            
            inner_attempts += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            inner_attempts += 1

    if inner_attempts == 3:
        print("Too many invalid inputs. Game over.")
        break

    for attempts in range(1, 4):  # Use a for loop to count attempts
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            score += 1
        else:
            print(f"Wrong guess. The correct number is {secret_number}. Your score for this question is decreased by 1.")
            score -= 1

        print(f"Your current score: {score}")
        break  # Exit the for loop after one iteration

    outer_attempts += 1