class ToDoList:
    def __init__(self):
        self.tasks = {}

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, (task, status) in enumerate(self.tasks.items(), start=1):
                print(f"{index}. [{status}] {task}")

    def add_task(self, task):
        self.tasks[task] = 'Incomplete'
        print(f"Task '{task}' added to the to-do list.")

    def mark_complete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = list(self.tasks.keys())[task_index - 1]
            self.tasks[task] = 'Complete'
            print(f"Task '{task}' marked as complete.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = list(self.tasks.keys())[task_index - 1]
            del self.tasks[task]
            print(f"Task '{task}' removed from the to-do list.")
        else:
            print("Invalid task index.")


def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            todo_list.display_tasks()
            task_index = int(input("Enter the index of the task to mark as complete: "))
            todo_list.mark_complete(task_index)
        elif choice == '4':
            todo_list.display_tasks()
            task_index = int(input("Enter the index of the task to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
