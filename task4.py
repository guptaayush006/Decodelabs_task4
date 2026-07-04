# General Knowledge Quiz Application

score = 0

# Question 1
answer = input("1. What is the capital of France? ").strip().lower()

if answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Paris.")

# Question 2
answer = input("\n2. Which planet is known as the Red Planet? ").strip().lower()

if answer == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Mars.")

# Question 3
answer = input("\n3. Who is known as the Father of Computer? ").strip().lower()

if answer == "charles babbage":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Charles Babbage.")

print("\nQuiz Completed!")
print(f"Your Final Score: {score}/3")
