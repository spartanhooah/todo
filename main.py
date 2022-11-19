def show_todos(todos_list):
    for index, item in enumerate(todos_list):
        print(f"{index + 1}: {item.strip()}")


def get_int_from_user(prompt):
    return int(input(prompt)) - 1


with open('todos.txt', 'r+') as file:
    all_todos = file.readlines()
    new_todos = []

    while True:
        user_action = input("Type 'add', 'show', 'edit', 'complete', or 'exit': ").strip().lower()

        if user_action.startswith('add'):
            if len(user_action) <= 4:
                continue

            todo = user_action[4:] + "\n"
            new_todos.append(todo)
            all_todos.append(todo)

        elif user_action.startswith('show'):
            show_todos(all_todos)

        elif user_action.startswith('edit'):
            show_todos(all_todos)
            index = get_int_from_user("Enter the number of the item to edit: ")

            if index > len(all_todos) or index < 1:
                print("That is not a valid choice.")
                continue

            new_todo = input("Enter the corrected todo: ") + "\n"
            all_todos[index] = new_todo

        elif user_action.startswith('complete'):
            show_todos(all_todos)
            index = get_int_from_user("Enter the number of completed item: ")

            if index > len(all_todos) or index < 1:
                print("That is not a valid choice.")
                continue

            all_todos.pop(index)

        elif user_action.startswith('exit'):
            file.writelines(new_todos)
            break
