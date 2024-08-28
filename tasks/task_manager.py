import streamlit as st
import pandas as pd  # Ensure pandas is imported

# Initialize session state attributes if they do not exist
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

def add_task(task_name):
    if task_name:
        st.session_state.tasks.append(task_name)
        st.success(f"Added '{task_name}' to the Todo List.")
        st.session_state.task_name = ""  # Clear the input field
    else:
        st.error("Task name can't be empty.")

def list_tasks():
    if st.session_state.tasks:
        st.write("## Todo List")
        tasks_df = pd.DataFrame(st.session_state.tasks, columns=["Tasks"])
        st.table(tasks_df)
    else:
        st.warning("Todo list is empty.")

def clear_tasks():
    if st.session_state.tasks:
        st.session_state.tasks.clear()
        st.success("Todo list cleared.")
    else:
        st.warning("Todo list is empty.")
