from task import Task
from todo_list import Todo_list

todo_list = Todo_list()
while True:
    print('---Welcome to the To-Do List App!---')
    print('1. Add a task')
    print('2. View tasks')
    print('3. Exit')

    choice = input('Enter your choice (1-3): ')

    if choice == '1':
        title = input('Enter task title: ')
        description = input('Enter task description: ')
        due_date = input('Enter task due date (YYYY-MM-DD): ')
        priority = input('Enter task priority (Low, Medium, High): ')
        print(f'Task added successfully!\n')
        todo_list.add_task(Task(title, description, due_date, priority))
        continue

    elif choice == '2':
        if todo_list.list_tasks():
            for task in todo_list.list_tasks():
                print(f'Title: {task["Title"]}')
                print(f'Description: {task["Description"]}')
                print(f'Due Date: {task["Due Date"]}')
                print(f'Priority: {task["Priority"]}')
                print('---\n')
        else:
            print('You have no tasks! Please first add a task.')
            print('---\n')
            continue

    elif choice == '3':
        print('Exiting the app. Goodbye!\n')
        break

    else:
        print('Invalid choice. Please try again.\n')