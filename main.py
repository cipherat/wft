#!./venv/bin/python3
from src import wft

if __name__ == "__main__":
    filename = "tasks.json" # Feature (#81AB01)
    with open(filename, 'r+') as file:
        wft.run(file)
