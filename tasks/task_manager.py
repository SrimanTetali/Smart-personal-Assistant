# Example of a simple task manager implementation
tasks = []

def add_task(task_description):
    tasks.append(task_description)
    return "Task added successfully."

def list_tasks():
    if not tasks:
        return "No tasks found."
    return "\n".join(tasks)
