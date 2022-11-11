def show_todos(todos_list):
    for index, item in enumerate(todos_list):
        print(f"{index + 1}: {item.strip()}")


with open('todos.txt', 'r+') as file:
    all_todos = file.readlines()
    new_todos = []

    while True:
        user_action = input("Type 'add', or 'show', 'edit', 'complete', or 'q': ").strip()

        match user_action:
            case 'add':
                todo = input("Enter a todo: ") + "\n"
                new_todos.append(todo)
                all_todos.append(todo)
            case 'show':
                show_todos(all_todos)
            case 'edit':
                show_todos(all_todos)
                number = int(input("Enter the number of the item to edit: ")) - 1
                new_todo = input("Enter a todo: ")
                all_todos[number] = new_todo
            case 'complete':
                show_todos(all_todos)
                number = int(input("Enter the number of completed item: ")) - 1
                all_todos.pop(number)
            case 'q':
                file.writelines(new_todos)
                break
