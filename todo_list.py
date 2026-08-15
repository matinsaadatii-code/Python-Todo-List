from task import Task

class Todo_list():
    def __init__(self):
        self.tasks = []

    def delete_task(self, name):
        for tk in self.tasks:
            if tk.title == name:
                self.tasks.remove(tk)
                return 'Task deleted.'

    def add_task(self, task):
        tk = {
            'Title': task.title,
            'Description': task.description,
            'Due Date': task.due_date,
            'Priority': task.priority,
        }
        self.tasks.append(tk)

    def list_tasks(self):
        return self.tasks
