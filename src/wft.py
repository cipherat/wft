from json import loads,dumps
from random import choice
from datetime import datetime


# utilities
def read_date():
    date = 0
    try:
        date = str(datetime.fromisoformat(_)) if (_ := input("date (YYYY-MM-DD): ")) else _ # ignore else
    except Exception as reason:
        print("[ERROR] Couldn't verify date, set to default(%d). Reason: %s" % (date, reason))
    finally:
        return date


# manage tasks files (json:w,r)
def readJsonFile(file):
    return loads(file.read())

def writeJsonFile(file, text):
    file.seek(0)
    file.truncate()
    return file.write(dumps(loads(text)))


# manage tasks (add, delete, edit)
def addTask(file, title, date):
    tasks = readJsonFile(file)
    try:
        tasks[title] = date
        writeJsonFile(file, dumps(tasks))
        print("[#] Task added successfully.")
    except Exception as reason:
        print("[ERROR]: Couldn't add task. Reason: %s" % reason)

def delTask(file, title):
    tasks = readJsonFile(file)
    try:
        del tasks[title]
        writeJsonFile(file, dumps(tasks))
        print("[#] Task deleted successfully.")
    except Exception as reason:
        print("[ERROR]: Couldn't delete task. Reason: %s" % reason)

def editTask(file, old_title, new_title, new_date):
    tasks = readJsonFile(file)
    try:
        tasks[new_title] = tasks.pop(old_title)
        if new_date:
            tasks[new_title] = new_date
        writeJsonFile(file, dumps(tasks))
        print("[#] Task edited successfully.")
    except Exception as reason:
        print("[ERROR]: Couldn't edit task. Reason: %s" % reason)

def showTasks(file):
    tasks = readJsonFile(file)
    print("%5s Tasks For Today %-5s" % ('=', '='))
    for i, task in enumerate(tasks):
        print("%d. %s" % (i+1, task))

def randomTask(file):
    tasks = readJsonFile(file)
    random = choice(list(tasks.keys()))
    print("[Random] %s (%s)" % (random, tasks[random]))


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
    option = input("> ")

    NUMBER_OF_CHOICES = 3
    match (option):
        case '1':
            title = input("task: ")
            date = read_date()
            addTask(file, title, date)
        case '2':
            old_title = input("old Task: ")
            new_title =  input("new Task: ")
            new_date = read_date()
            editTask(file, old_title, new_title, new_date)
        case '3':
            title = input("task: ")
            print("Are you sure you want to delete (%s) ['enter' for no]: " % (title), end='')
            if bool(input("")):
                delTask(file, title)
        case _:
            print("[ERROR]: Invalid Choice (1-%d)" % NUMBER_OF_CHOICES)


# manages user I/O
def run(tasks_file):
    print("# What For Today?")
    displayMenu()
    option = input("> ")

    NUMBER_OF_CHOICES = 3
    match (option):
        case '1':
            showTasks(tasks_file)
        case '2':
            randomTask(tasks_file)
        case '3':
            manageTasks(tasks_file)
        case _:
            print("[ERROR]: Invalid Choice (1-%d)" % NUMBER_OF_CHOICES)

