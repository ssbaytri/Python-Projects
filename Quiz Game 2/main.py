# Quiz Game (Advanced)

questions = (
    "What is the capital of France?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the chemical symbol for water?",
    "Which planet is known as the Red Planet?",
    "What is the largest mammal in the world?"
)

options = (
    ("A. Berlin", "B. London", "C. Paris", "D. Madrid"),
    ("A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"),
    ("A. N2", "B. CO2", "C. O2", "D. H2O"),
    ("A. Saturn", "B. Venus", "C. Jupiter", "D. Mars"),
    ("A. Blue Whale", "B. Elephant", "C. Giraffe", "D. Great White Shark")
)

answers = ("C", "B", "D", "D", "A")
guesses = []
score = 0
question_number = 0

for question in questions:
    print("-----------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    guess = input("Pick Up (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"The correct answer is {answers[question_number]}")
    question_number += 1

print("-----------------------")
print("        RESULTS        ")
print("-----------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

