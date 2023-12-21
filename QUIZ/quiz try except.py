def ask_question(question, correct_answer):
    try:
        user_answer = input(question + " ").lower()
        
        # Check if the user's answer is correct
        if user_answer == correct_answer.lower():
            print("Correct!\n")
            return True
        else:
            print("Incorrect. The correct answer is '{}'.".format(correct_answer))
            return False

    except KeyboardInterrupt:
        print("\nQuiz interrupted. Exiting...")
        exit()

def quiz():
    score = 0

    # Define your questions and answers
    questions_and_answers = [
        ("What is the capital of France?", "Paris"),
        ("Which planet is known as the Red Planet?", "Mars"),
        ("What is the largest mammal in the world?", "Blue Whale"),
        # Add more questions as needed
    ]

    # Ask each question and update the score
    for question, answer in questions_and_answers:
        try:
            if ask_question(question, answer):
                score += 1
        except Exception as e:
            print("An error occurred:", e)

    print("Quiz completed! Your final score is {}/{}".format(score, len(questions_and_answers)))

if __name__ == "__main__":
    print("Welcome to the Quiz Game!\n")
    quiz()