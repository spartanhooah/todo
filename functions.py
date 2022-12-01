FILEPATH = "todos.txt"


def show_todos(todos_list):
    """ Given a list of todos, print out an enumerated list. """
    for i, item in enumerate(todos_list):
        print(f"{i + 1}: {item.strip()}")


def get_int_from_user(prompt):
    """ Prompt the user for input. Convert the input to an
     integer, then subtract one from it (for 1-based indexing).
     """
    return int(input(prompt)) - 1


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items """
    with open(filepath, 'r') as file:
        return file.readlines()


def write_todos(todos, filepath=FILEPATH):
    """ Write the to-do items list in the  text file """
    with open(filepath, 'w') as file:
        file.writelines([todo + "\n" for todo in todos])
