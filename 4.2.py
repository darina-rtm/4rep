question = "Solve this: 4 * 100 - 54"
correct_answer = 4 * 100 - 54

print(question)
user_answer = int(input("Your answer: "))

if user_answer == correct_answer:
    print("Correct!")
else:
    print(f"Incorrect. The correct answer is {correct_answer}.")
