import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Add a todo",
              label_visibility="hidden",
              placeholder="Add a new to-do...")
