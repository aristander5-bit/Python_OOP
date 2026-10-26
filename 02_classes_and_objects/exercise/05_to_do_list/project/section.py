from project.task import Task

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        task = next((t for t in self.tasks if t.name == task_name), None)
        if task:
            task.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        curr_task_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        return f"Cleared {curr_task_len - len(self.tasks)} tasks."

    def view_section(self):
        details = "\n".join([t.details() for t in self.tasks])
        return f"Section {self.name}:\n{details}"