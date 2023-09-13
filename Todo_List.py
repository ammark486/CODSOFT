class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def update_task(self, index, new_task):
        if index < len(self.tasks):
            self.tasks[index] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def remove_task(self, index):
        if index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print("Task removed successfully:", removed_task)
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks found.")


def print_menu():
    print("===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Remove Task")
    print("4. Display Tasks")
    print("5. Exit")


def main():
    todo_list = TodoList()

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter the task index to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == "3":
            index = int(input("Enter the task index to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()