import time

class QuizGame:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "London"], "answer": "Paris"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter"], "answer": "Mars"},
            {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe"], "answer": "Blue Whale"}
            # Add more questions as needed
        ]
        self.score = 0
        self.time_limit = 10  # Time limit per question in seconds

    def ask_question(self, question_data):
        print(question_data["question"])
        for i, option in enumerate(question_data["options"], start=1):
            print(f"{i}. {option}")

    def run_quiz(self):
        print("Welcome to the Quiz Game!")
        time.sleep(1)

        for question_data in self.questions:
            self.ask_question(question_data)

            while True:  # Introduce a while loop for retrying a question
                start_time = time.time()

                try:
                    user_answer = input("Your answer (enter the option number, 'skip' to skip): ")

                    if user_answer.lower() == 'skip':
                        print("Question skipped! Score remains unchanged.\n")
                        break  # Exit the while loop and move to the next question

                    user_answer_index = int(user_answer) - 1
                    selected_option = question_data["options"][user_answer_index]

                    if selected_option == question_data["answer"]:
                        print("Correct! You earned 1 point.\n")
                        self.score += 1
                        break  # Exit the while loop and move to the next question
                    else:
                        print(f"Wrong! The correct answer is {question_data['answer']}. Score decreased by 1.\n")
                        self.score -= 1
                        # Allow the user to retry the question within the while loop

                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid option or 'skip'.\n")
                    continue  # Allow the user to retry the question within the while loop

                elapsed_time = time.time() - start_time
                time_left = max(0, self.time_limit - elapsed_time)

                if time_left == 0:
                    print("Time's up! Moving to the next question.\n")
                else:
                    print(f"Time left: {time_left:.2f} seconds\n")

                time.sleep(1)  # Add a pause before the next question

        print("Quiz completed!")
        print(f"Your final score: {self.score}")

if __name__ == "__main__":
    quiz_game = QuizGame()
    quiz_game.run_quiz()