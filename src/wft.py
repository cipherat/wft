from .ui import *
from .utils import *
from .manager import *

def run(tasks_file):
    NUMBER_OF_CHOICES = display_menu()
    option = input("> ")

    match (option):
        case '1':
            show_tasks(tasks_file)
        case '2':
            random_task(tasks_file)
        case '3':
            manage_tasks(tasks_file)
        case _:
            print("[ERROR]: Invalid Choice (1-%d)" % NUMBER_OF_CHOICES)

