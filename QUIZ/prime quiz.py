import random

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_game():
    score = 0
    num_questions = 5  # You can adjust the number of questions as desired

    print("Welcome to the Prime Number Game!")
    print("Answer 'yes' if the number is prime, and 'no' if it's not.\n")

    for _ in range(num_questions):
        current_number = random.randint(1, 100)  # Adjust the range as desired
        correct_answer = is_prime(current_number)
        
        print(f"Is {current_number} a prime number?")
        user_input = input("Your answer (yes/no): ").lower()

        if (user_input == 'yes' and correct_answer) or (user_input == 'no' and not correct_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {'yes' if correct_answer else 'no'}.\n")

    print(f"Game over! Your score: {score}/{num_questions}")

if __name__ == "__main__":
    prime_game()