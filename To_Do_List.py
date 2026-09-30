# Python Mini Project TO DO LIST 

# Empty List

tasks = []

def add_task():

    task = input("Enter Task: ")

    tasks.append({
        "task": task,
        "completed": False

    })

    print("Task Added Successfully!")


def view_tasks():

    if not tasks:
        print("No Tasks Found.")
        return

    print("\n--- To Do List ---")

    for index, task in enumerate(tasks,start=1):
        status = "Complete" if task["completed"] else "Pending"

        print(f"{index}. {task["task"]} - {status}")

def complete_task():
    view_tasks()

    if not tasks():
        return

    number = int(input("Enter Task Number to Complete: "))

    if 1 <= number <= len(tasks):
        tasks[number - 1]["completed"] = True
        print("Task Marked is Completed!")
    else:
        print("Invalid task Number.")
        
def delete_task():
    view_tasks()

    if not tasks:
        return

    number = int(input("Enter Task Number to Delete: "))

    if 1 <= number <= len(tasks):
        removed_task = tasks.pop(number - 1)
        print(f"Task '{removed_task['task']}' Deleted Successfully!  ")
    else:
        print("Invalid task Number.")

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please try again.")

        
add_task()
add_task()

complete_task()

delete_task()

view_tasks()

