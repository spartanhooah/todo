prompt = "Enter a todo: "
todos = []

while True:
    todo = input(prompt)

    if todo == 'q':
        break

    todos.append(todo)

print(todos)
