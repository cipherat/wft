from json import dumps, loads
from datetime import datetime


def init_file(filename):
    with open(filename, 'w+') as fd:
        fd.write("{}")
    return filename


def read_date():
    date = 0
    try:
        date = str(datetime.fromisoformat(_)) if (_ := input("date (YYYY-MM-DD): ")) else 0

    except Exception as reason:
        print("[ERROR] Couldn't verify date, set to default(%d). Reason: %s" % (date, reason))

    finally:
        return date


# manage tasks files (json:w,r)
def read_json_file(file):
    return loads(file.read())

def write_json_file(file, text):
    file.seek(0)
    file.truncate()
    return file.write(dumps(loads(text)))
