#!/usr/bin/env python3
from src import wft

def init_file(filename):
    with open(filename, 'w+') as fd:
        fd.write("{}")
    return filename

if __name__ == "__main__":
    filename = "tasks.json"
    if _fn:=input("use file (Enter for default '%s'): " % (filename)):
        filename = init_file(_fn)

    with open(filename, 'r+') as file:
        wft.run(file)
