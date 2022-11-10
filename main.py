todos = []

while True:
    user_action = input("Type 'add', or 'show', 'edit', or 'q': ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            i = 1
            for item in todos:
                print("{}: {}".format(i, item))
                i = i + 1
        case 'edit':
            number = int(input("Enter the number of the item to edit: ")) - 1
            to_edit = todos[number]
            new_todo = input("Enter a todo: ")
            todos[number] = new_todo
        case 'q':
            break
