from termcolor import colored
todo_list = []

def show_task():
    if not todo_list:
        print(colored("No tasks in the list.", "yellow"))
    else:
        for index, task in enumerate(todo_list, 1):
            print(colored(f"{index}. {task}", "yellow"))

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print(colored(f"Task \"{task}\" added to to_do list", "green"))

def delete_task():
    show_task()
    if not todo_list:
        return "The list is empty"
    try:
        index = int(input("Enter the task number to delete"))
        if 1 <= index <= len(todo_list):
            removed = todo_list.pop(index - 1) # as indexing starts from 0
            print(colored(f"Task '{removed}' deleted.", "red"))
        else:
            print("Invalid Task number")
    except ValueError:
        print("Please enter a valid number")


while True:
    print("\n=== To-Do List ===")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Quit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        show_task()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
