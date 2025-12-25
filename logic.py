import csv

# It stores the information of each task. (representative of each task)
class Task:
    def __init__(self, title, description, priority):
        priorities = ["high", "medium", "low"]
        if priority not in priorities:
            raise ValueError(f"Invalid priority '{priority}'. Choose from {priorities}.")
        self.title = title
        self.description = description
        self.priority = priority

    # It returns the task information as a tuple.
    def get_data(self):
        return self.title, self.description, self.priority

    def show(self):
        print(f"Title: {self.title}, Description: {self.description}, Priority: {self.priority}")

    # Setting priorities, to implement correctly.
    def get_priority_weight(self):
        mapping = {"high": 3, "medium": 2, "low": 1}
        return mapping.get(self.priority, 0)

# Responsible for managing tasks.
class ToDoList:
    def __init__(self):
        self.tasks = []

    # Add a new task.
    def add_task(self, task):
        self.tasks.append(task)
        self.sort_tasks()

    # Sort tasks according to their priority.
    def sort_tasks(self):
        self.tasks.sort(key=lambda t: t.get_priority_weight(), reverse=True)

    # Show all tasks.
    def show_tasks(self):
        if not self.tasks:
            print("No tasks to show.\n")
            return
        self.sort_tasks()
        for task in self.tasks:
            task.show()

    # Filter tasks based on priority.
    def filter_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    # Counting the number of tasks based on priority.
    def count_by_priority(self):
        counts = {"high": 0, "medium": 0, "low": 0}
        for task in self.tasks:
            if task.priority in counts:
                counts[task.priority] += 1
        return counts
    
    # Remove the task from the list.
    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False

    # Save tasks in CSV file.
    def save_to_csv(self, filename):
        try:
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Description", "Priority"])
                for task in self.tasks:
                    writer.writerow(task.get_data())
            return True
        except Exception as e:
            print(f"Error saving tasks to '{filename}': {e}")
            return False
        
    # load from the csv file and add to the list of tasks.
    def load_from_csv(self, filename):
        try:
            self.tasks = []
            with open(filename, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)  # skip header
                for row in reader:
                    if len(row) == 3:
                        try:
                            task = Task(row[0], row[1], row[2])
                            self.tasks.append(task)
                        except ValueError as ve:
                            print(f"Skipping invalid task: {ve}")
            self.sort_tasks()
            return True
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return False
        except Exception as e:
            print(f"Error loading tasks from '{filename}': {e}")
            return False
