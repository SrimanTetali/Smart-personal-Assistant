import sys
import os

# Add the parent directory of 'ui' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from tasks import task_manager
from speech import speech_to_text as stt
from speech import text_to_speech as tts

def add_task():
    task_description = st.text_input("Enter task description:")
    if st.button("Add Task"):
        if task_description:
            response = task_manager.add_task(task_description)
            st.success(response)
        else:
            st.warning("Please enter a task description.")

def list_tasks():
    if st.button("List Tasks"):
        response = task_manager.list_tasks()
        st.text(response)

def use_voice_recognition():
    if st.button("Start Voice Recognition"):
        text = stt.speech_to_text()
        st.write(f"Recognized Text: {text}")
        if text:
            tts.text_to_speech(text)
            
def main():
    st.title("Smart Personal Assistant")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    option = st.sidebar.selectbox("Choose an action:", ["Add Task", "List Tasks", "Voice Recognition"])
    
    if option == "Add Task":
        add_task()
    elif option == "List Tasks":
        list_tasks()
    elif option == "Voice Recognition":
        use_voice_recognition()

if __name__ == "__main__":
    main()
