import functions
import PySimpleGUI as sg


def get_stripped_todos():
    return [todo.strip() for todo in functions.get_todos()]


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", bind_return_key=True)
list_box = sg.Listbox(values=get_stripped_todos(),
                      key="todos",
                      enable_events=True,
                      size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 14))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = get_stripped_todos()
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)

            window["todos"].update(values=todos)
        case "Edit":
            to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"

            todos = get_stripped_todos()
            index = todos.index(to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)

            window["todos"].update(values=todos)
        case "Complete":
            to_complete = values["todos"][0]

            todos = get_stripped_todos()
            index = todos.remove(to_complete)
            functions.write_todos(todos)

            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Exit":
            break
        case "todos": # update input box when clicking a todo
            window["todo"].update(value=values["todos"][0])
        case sg.WINDOW_CLOSED:
            break

window.close()
