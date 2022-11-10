todos = []


def show_todos():
    for index, item in enumerate(todos):
        print(f"{index + 1}: {item}")


while True:
    user_action = input("Type 'add', or 'show', 'edit', 'complete', or 'q': ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            show_todos()
        case 'edit':
            show_todos()
            number = int(input("Enter the number of the item to edit: ")) - 1
            new_todo = input("Enter a todo: ")
            todos[number] = new_todo
        case 'complete':
            show_todos()
            number = int(input("Enter the number of completed item: ")) - 1
            todos.pop(number)
        case 'q':
            break
