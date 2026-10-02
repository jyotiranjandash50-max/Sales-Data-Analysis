import json 
import os

FILE_Name = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_Name):
        return []
    try:
        with open (FILE_Name, "I") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(FILE_Name, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for index, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} [{status}]")

def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to mark as donr: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("invalid task number.")
    except ValueError:
        print("please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task['title']}' deleted successfully!")
        else:
            print("invalid task number.")
    except ValueError:
        print("please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. mark Task as done")
        print("4. Delete Task")
        print("5. Exit" )

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("invalid choice. Please try again.")

if __name__ == "__main__":
    main()