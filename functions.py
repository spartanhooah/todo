def show_todos(todos_list):
    """ Given a list of todos, print out an enumerated list. """
    for i, item in enumerate(todos_list):
        print(f"{i + 1}: {item.strip()}")


def get_int_from_user(prompt):
    """ Prompt the user for input. Convert the input to an
     integer, then subtract one from it (for 1-based indexing).
     """
    return int(input(prompt)) - 1
