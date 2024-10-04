#!/usr/bin/env python3
from src import wft, utils


if __name__ == "__main__":
    filename = "tasks.json"

    if _fn:=input("use file (Enter for default '%s'): " % (filename)): # use given input, otherwise -empty- skip
        filename = utils.init_file(_fn)

    with open(filename, 'r+') as file:
        wft.run(file)
