from json import loads,dumps
from random import choice


# manage tasks files (json:w,r)
def readJsonFile(file):
    return loads(file.read())

def writeJsonFile(file, text):
    file.seek(0)
    file.truncate()
    return file.write(dumps(loads(text)))


# manage tasks (add, delete, edit)
def addTask(file, title):   # Feature (#81AB01)
    tasks = readJsonFile(file)
    tasks[title] = 0
    writeJsonFile(file, dumps(tasks))

def delTask(file, title):
    tasks = readJsonFile(file)
    del tasks[title]
    writeJsonFile(file, dumps(tasks))

def editTask(file, old_title, new_title): # Feature (#81AB01)
    tasks = readJsonFile(file)
    tasks[new_title] = tasks.pop(old_title)
    writeJsonFile(file, dumps(tasks))

def showTasks(file):
    tasks = readJsonFile(file)
    print("%5s Tasks For Today %-5s" % ('=', '='))
    for i, task in enumerate(tasks):
        print("%d. %s" % (i+1, task))

def randomTask(file):
    tasks = readJsonFile(file)
    random = choice(list(tasks.keys()))
    print("[Random] %s" % (random))


# user interface (TUI)
def displayMenu():
    print("[1] Show Tasks")
    print("[2] Random Task")
    print("[3] Manage Tasks")

def displayTaskMng():
    print("[1] Add Task")
    print("[2] Edit Task")
    print("[3] Remove Task")

def manageTasks(file):
    displayTaskMng()
    option = int(input("> "))   # Bug (#172E2A)
    
    match (option):
        case 1:
            title = input("task: ")
            addTask(file, title)
        case 2:
            old_title, new_title = input("old_task,new_task: ").split(',')
            editTask(file, old_title, new_title)
        case 3:
            title = input("task: ")
            print("Are you sure you want to delete (%s) [0/1]: " % (title), end='')
            if int(input("")):  # Bug (#172E2A)
                delTask(file, title)
        case _:
            print("[ERROR]: Invalid Choice (1-3)")


# manages user I/O
def run(tasks_file):
    print("# What For Today?")
    displayMenu()
    option = int(input("> "))   # Bug (#172E2A)
    
    match (option):
        case 1:
            showTasks(tasks_file)
        case 2:
            randomTask(tasks_file)
        case 3:
            manageTasks(tasks_file)
        case _:
            print("[ERROR]: Invalid Choice (1-3)")

