# TASK MANAGER
# it manages the tasks.

# Task list:
task_list = []

while True:
    command = input("$TASK-MANAGER: ")

    if command == "close":
        break

    elif command == "ls":
        if len(task_list) == 0:
            print("There is no task added.")
        else:
            for task in range(len(task_list)):
                print(f"{task + 1}. {task_list[task]}")

    elif command == "add":
        task_list.append(input("$TASK: "))
        print("TASK is successfully added to the list.")

    elif command == "delete":
        search = input("Search task: ")

        if search in task_list:
            task_list.remove(search)
            print("Task is successfully deleted.")
        else:
            print("Task not found.")


    elif command == "": 
        pass

    elif command == "help":
        print("1. ls: list all tasks")
        print("2. add: add task")
        print("3. delete: delete task")
        print("4. close: break the loop")

        
    else:
        print("Wrong command.")
