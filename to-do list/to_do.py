tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your To Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def edit_task(index, new_task):
    if 0 <= index-1 < len(tasks):
        print(f"Task '{tasks[index-1]}' updated to '{new_task}'.")
        tasks[index-1] = new_task
    else:
        print("Invalid task number.")

def delete_task(index):
    if 0 <= index-1 < len(tasks):
        print(f"Task '{tasks[index-1]}' deleted.")
        tasks.pop(index-1)
    else:
        print("Invalid task number.")

while(True):
    ch = int(input("Enter your choice(1/2/3/4/5)- 1.add_task 2.view_task 3.edit_task 4.delete_task 5.exit:"))

    if ch==1:
        task = input("Enter task:")
        add_task(task)
    elif ch==2:
        view_tasks()
    elif ch==3:
        index = int(input("Enter index where you want to edit:"))
        new_task = input("Enter a new task:")
        edit_task(index, new_task)
    elif ch==4:
        ind = int(input("Enter a index for deleting task:"))
        delete_task(ind)
    elif ch==5:
        break
