from json import dumps
from random import choice

from .utils import *


def add_task(file, title, date):
    tasks = read_json_file(file)
    try:
        tasks[title] = date
        write_json_file(file, dumps(tasks))
        print("[#] Task added successfully.")

    except Exception as reason:
        print("[ERROR]: Couldn't add task. Reason: %s" % reason)


def del_task(file, title):
    tasks = read_json_file(file)
    try:
        del tasks[title]
        write_json_file(file, dumps(tasks))
        print("[#] Task deleted successfully.")

    except Exception as reason:
        print("[ERROR]: Couldn't delete task. Reason: %s" % reason)


def edit_task(file, old_title, new_title, new_date):
    tasks = read_json_file(file)
    try:
        tasks[new_title] = tasks.pop(old_title)
        if new_date:
            tasks[new_title] = new_date
        write_json_file(file, dumps(tasks))
        print("[#] Task edited successfully.")

    except Exception as reason:
        print("[ERROR]: Couldn't edit task. Reason: %s" % reason)


def show_tasks(file):
    tasks = read_json_file(file)
    print("%5s Tasks For Today %-5s" % ('=', '='))

    for i, task in enumerate(tasks):
        print("%d. %s (%s)" % (i+1, task, tasks[task]))


def random_task(file):
    tasks = read_json_file(file)
    random = choice(list(tasks.keys()))
    print("[Random] %s (%s)" % (random, tasks[random]))
