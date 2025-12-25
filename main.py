from logic import Task, ToDoList

# User selection from among the items in the program.
def menu():
    print("--------------------------------")
    print("===== To-Do List Menu =====")
    menu_items = [
        "Show tasks.",
        "Add task.",
        "Delete task.",
        "Save to CSV file.",
        "Load from CSV file.",
        "Filter tasks by priority.",
        "Show task counts by priority",
        "Exit."
    ]

    for i, item in enumerate(menu_items, 1):
        print(f"{i}. {item}")
    print("--------------------------------")

    while True:
        choice = input("Enter your choice (1-8): ")
        if choice.isdigit() and 1 <= int(choice) <= 8:
            return int(choice)
        else:
            print("Please enter a valid number between 1 and 8.")

# Responsible for managing operations and displaying appropriate messages based on user selections and inputs.
def main():
    todo = ToDoList()
    current_file = None

    while True:
        choice = menu()

        if choice == 1:
            print("----Tasks----")
            todo.show_tasks()
            print("\n")

        elif choice == 2:
            title = input("Title for Task: ")
            description = input("Description for Task: ")
            priorities = ["high", "medium", "low"]
            priority = input("Task Priority (high/medium/low): ").lower()
            while priority not in priorities:
                print("Please choose from (high/medium/low)")
                priority = input("Task Priority (high/medium/low): ").lower()
            try:
                task = Task(title, description, priority)
                todo.add_task(task)
                print("Task added.\n")
            except ValueError as ve:
                print(f"Error adding task: {ve}")

        elif choice == 3:
            title = input("To delete a task, Enter the title of the task: ")
            removed = todo.remove_task(title)
            if removed:
                print("Task removed successfully.")
            else:
                print("No task with this title was found.")

        elif choice == 4:
            filename = input("Enter the name of the CSV file to save: ")
            saved = todo.save_to_csv(filename)
            if saved:
                current_file = filename
                print(f"Tasks successfully saved to {filename} and now working on this file.")
            else:
                print("Error saving tasks to file.")

        elif choice == 5:
            filename = input("Enter the name of the CSV file to load: ")
            loaded = todo.load_from_csv(filename)
            if loaded:
                current_file = filename
                print(f"Tasks successfully loaded from {filename}")
            else:
                print("Error loading tasks. File may not exist or be invalid.")

        elif choice == 6:
            priority = input("Enter priority to filter (high/medium/low): ").lower()
            while priority not in ["high", "medium", "low"]:
                print("Invalid priority.")
                priority = input("Enter priority to filter (high/medium/low): ").lower()
            
            filtered_tasks = todo.filter_by_priority(priority)
            print(f"Tasks with priority '{priority}':")
            if not filtered_tasks:
                print(" (None!) ")
            else:
                for task in filtered_tasks:
                    task.show()

        elif choice == 7:
            counts = todo.count_by_priority()
            print("Task counts by priority:")
            print(f"High   : {counts['high']}")
            print(f"Medium : {counts['medium']}")
            print(f"Low    : {counts['low']}")

        # Automatic saving of the current file when exiting.
        elif choice == 8:
            if current_file:
                todo.save_to_csv(current_file)
                print(f"Tasks automatically saved to {current_file}.")
            else:
                todo.save_to_csv("todolist.csv")
                print("Tasks automatically saved to todolist.csv.")
            print("Exited the program.")
            break


if __name__ == "__main__":
    main()
