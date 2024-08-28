import streamlit as st
import sys
import os

# Add the parent directory of the 'tasks' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tasks.task_manager import add_task, list_tasks, clear_tasks
import speech_recognition as sr

def voice_recognition():
    st.write("## Voice Recognition")
    if st.button('Start Listening'):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                st.write(f"You said: {text}")
            except sr.UnknownValueError:
                st.write("Sorry, I did not understand that.")
            except sr.RequestError:
                st.write("Sorry, there was a problem with the request.")

def main():
    st.sidebar.title("Navigation")
    option = st.sidebar.radio("Select Page", ("Todo", "Voice Recognition"))

    if option == "Todo":
        st.title("Todo Page")

        # Input for task name
        task_name = st.text_input("Enter task name", key="task_input")

        # Buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Add Task"):
                add_task(task_name)
        with col2:
            if st.button("List Tasks"):
                list_tasks()
        with col3:
            if st.button("Clear Todo List"):
                clear_tasks()

    elif option == "Voice Recognition":
        voice_recognition()

if __name__ == "__main__":
    main()
