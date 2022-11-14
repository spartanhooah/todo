def show_todos(todos_list):
    for index, item in enumerate(todos_list):
        print(f"{index + 1}: {item.strip()}")


def get_int_from_user(prompt):
    return int(input(prompt)) - 1


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
                index = get_int_from_user("Enter the number of the item to edit: ")
                new_todo = input("Enter the corrected todo: ") + "\n"
                all_todos[index] = new_todo
            case 'complete':
                show_todos(all_todos)
                index = get_int_from_user("Enter the number of completed item: ")
                all_todos.pop(index)
            case 'q':
                file.writelines(new_todos)
                break
