lst = []
message = f"""
1 - add tasks to a list
2 - mark task as complete
3 - view tasks
4 - quit
"""
def addTask():
    task = input("Enter the task u want to add: ")
    task_info = {"Task" : task, "Completed" : False}
    lst.append(task_info)
    print("Task added to list successfully")
    print('-'*30)

def markComplete():
    incompleted_task = [task for task in lst if task["Completed"] == False]
    if len(incompleted_task) == 0:
        print("U need to add task to mark as completed.❤️")
        return
    
    for i,task in enumerate(incompleted_task):
        print(f"{i + 1}. {task["Task"]}")

    numTask = int(input("Enter the task u want to check as completed: "))
    incompleted_task[numTask - 1]["Completed"] = True
    print(f'{incompleted_task[numTask - 1]["Task"]} Checked as completed Well Done!😊')
    print('-'*30)


def viewTask():
    for i,task in enumerate(lst):
        print(f"""{i + 1}. {task["Task"]} {"✔️" if task["Completed"] == True  else "❌"}""")
    print('-'* 30)

while True:
    print(message)
    choice = int(input("Enter ur choice: "))
    if choice == 1:
        addTask()
    elif choice == 2:
        markComplete()
    elif choice == 3:
        viewTask()
    elif choice == 4:
        break
    else:
        print(f"Invalid choice please re-Enter number from 1 -> 4")
