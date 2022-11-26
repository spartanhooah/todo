import json

with open("questions.json", 'r') as file:
    file_content = file.read()

data = json.loads(file_content)

score = 0

for question in data:
    print(question["question_text"])

    for index, choice in enumerate(question["choices"]):
        print(index + 1, "-", choice)

    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

    if user_choice == question["answer"]:
        score += 1

    print()

for question in data:
    message = f"Your answer: {question['user_choice']} \n" \
              f"Correct answer: {question['answer']}"

    print(message)

print(f"\nYou scored {score} of {len(data)}")


