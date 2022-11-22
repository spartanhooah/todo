import functions

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
            functions.show_todos(all_todos)

        elif user_action.startswith('edit'):
            functions.show_todos(all_todos)
            index = functions.get_int_from_user("Enter the number of the item to edit: ")

            if index > len(all_todos) or index < 1:
                print("That is not a valid choice.")
                continue

            new_todo = input("Enter the corrected todo: ") + "\n"
            all_todos[index] = new_todo

        elif user_action.startswith('complete'):
            functions.show_todos(all_todos)
            index = functions.get_int_from_user("Enter the number of completed item: ")

            if index > len(all_todos) or index < 1:
                print("That is not a valid choice.")
                continue

            all_todos.pop(index)

        elif user_action.startswith('exit'):
            file.writelines(new_todos)
            break
