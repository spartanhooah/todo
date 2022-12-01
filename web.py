import streamlit as st
import functions

todos = [todo.strip() for todo in functions.get_todos()]


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")

for index, todo in enumerate(todos):
    st.checkbox(todo, key=index)

st.text_input(label="Add a todo",
              label_visibility="hidden",
              placeholder="Add a new to-do...",
              on_change=add_todo,
              key="new_todo")


