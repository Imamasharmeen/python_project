import json

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {'[x]' if task['completed'] else '[ ]'} {task['task']}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
        else:
            print("Invalid task index")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
        else:
            print("Invalid task index")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print("File not found")


def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List Manager =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Save Tasks to File")
        print("6. Load Tasks from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "5":
            filename = input("Enter filename to save tasks: ")
            todo_list.save_to_file(filename)
        elif choice == "6":
            filename = input("Enter filename to load tasks from: ")
            todo_list.load_from_file(filename)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
