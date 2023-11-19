import streamlit as st
import functions as func

todos = func.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    if todo_local not in todos:
        todos.append(todo_local)
        func.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",
              placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")
