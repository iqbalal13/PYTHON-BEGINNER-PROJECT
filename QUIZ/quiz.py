print("Welcome to the Python Quiz!")
score = 0
question_num = 1

# Question 1
print("\nQuestion", question_num)
print("What is the capital of France?")
print("A. London")
print("B. Paris")
print("C. Rome")
answer = input("Your answer: ")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Sorry, the correct answer is B. Paris.")
question_num += 1

# Question 2
print("\nQuestion", question_num)
print("What is the largest planet in our solar system?")
print("A. Earth")
print("B. Saturn")
print("C. Jupiter")
answer = input("Your answer: ")
if answer == "c":
    print("Correct!")
    score += 1
else:
    print("Sorry, the correct answer is C. Jupiter.")
question_num += 1

print("\nQuestion", question_num)
print("What is the largest mammal in the world?")
print("A. Elephant")
print("B. Whale")
print("C. Giraffe")
answer = input("Your answer: ")
if answer == "b":
    print("Correct!")
    score += 1
else:
    print("Sorry, the correct answer is B. Whale.")
question_num += 1

print("\nQuiz complete!")
print("You scored", score, "out of", question_num - 1, "questions.")