import functions
import PySimpleGUI as sg
import os


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


def get_stripped_todos():
    return [todo.strip() for todo in functions.get_todos()]


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(image_source=functions.resource_path("add.png"),
                       bind_return_key=True,
                       tooltip="Add a to-do",
                       key="add")
list_box = sg.Listbox(values=get_stripped_todos(),
                      key="todos",
                      enable_events=True,
                      size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_source=functions.resource_path("complete.png"),
                            tooltip="Complete the selected to-do",
                            key="complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 14))

while True:
    event, values = window.read()

    match event:
        case "add":
            todos = get_stripped_todos()
            todos.append(values["todo"])
            functions.write_todos(todos)

            window["todos"].update(values=todos)
        case "Edit":
            new_todo = values["todo"]
            todos = get_stripped_todos()

            try:
                to_edit = values["todos"][0]
                index = todos.index(to_edit)
                todos[index] = new_todo
            except IndexError:
                sg.PopupError("Please select an item first.", font=("Helvetica", 14))

            functions.write_todos(todos)

            window["todos"].update(values=todos)
        case "complete":
            todos = get_stripped_todos()

            try:
                to_complete = values["todos"][0]
                index = todos.remove(to_complete)
            except IndexError:
                sg.PopupError("Please select an item first.", font=("Helvetica", 14))

            functions.write_todos(todos)

            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Exit":
            break
        case "todos":  # update input box when clicking a todo
            window["todo"].update(value=values["todos"][0])
        case sg.WINDOW_CLOSED:
            break

window.close()
