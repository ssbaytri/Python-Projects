print("Welcome to the Quiz Game!")

playing = input("Would you like to play? (yes/no): ")
print("-" * 20)
score = 0

if playing.lower() != "yes":
    quit()

print("Great, Let's Start!")
print("-" * 20)

answer1 = input("what does RAM stand for? ")
if answer1.lower() == "random access memory":
    print("Correct!")
    score += 1
    print("-" * 20)
else:
    print("Incorrect!")
    print("-" * 20)

answer2 = input("what does ROM stand for? ")
if answer2.lower() == "read only memory":
    print("Correct!")
    score += 1
    print("-" * 20)
else:
    print("Incorrect!")
    print("-" * 20)

answer3 = input("what does GPU stand for? ")
if answer3.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
    print("-" * 20)
else:
    print("Incorrect!")
    print("-" * 20)

answer4 = input("what does CPU stand for? ")
if answer4.lower() == "central processing unit":
    print("Correct!")
    score += 1
    print("-" * 20)
    print(f"Your score is {score}")
else:
    print("Incorrect!")
    print("-" * 20)
    print(f"Your score is {score}")