from .utils import *
from .manager import *


def display_menu():
    print("# What For Today?")
    print("[1] Show Tasks")
    print("[2] Random Task")
    print("[3] Manage Tasks")
    return 3


def display_task_mng():
    print("[1] Add Task")
    print("[2] Edit Task")
    print("[3] Remove Task")
    return 3


def manage_tasks(file):
    NUMBER_OF_CHOICES = display_task_mng()
    option = input("> ")

    match (option):
        case '1':
            title = input("task: ")
            date = read_date()
            add_task(file, title, date)

        case '2':
            old_title = input("old Task: ")
            new_title =  input("new Task: ")
            new_date = read_date()
            edit_task(file, old_title, new_title, new_date)

        case '3':
            title = input("task: ")
            print("Are you sure you want to delete '%s' ['enter' for no]: " % (title), end='')
            if bool(input("")):
                del_task(file, title)
            else:
                print("[#] Task delete declined.")

        case _:
            print("[ERROR]: Invalid Choice (1-%d)" % NUMBER_OF_CHOICES)
