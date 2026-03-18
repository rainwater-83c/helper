import json
import os
import time
import datetime
import math


def make_userfile(userid, filename):
    if not os.path.exists(f"data/users/{userid}"):
        os.makedirs(f"data/users/{userid}")
    with open(f"data/users/{userid}/{filename}.json", "w") as f:
        f.write("{}")
        return json.loads("{}")


def get_userfile(userid, filename):
    if not os.path.exists(f"data/users/{userid}/{filename}.json"):
        make_userfile(userid, filename)
    with open(f"data/users/{userid}/{filename}.json", "r") as f:
        return json.load(f)


def set_userfile(userid, filename, contents):
    with open(f"data/users/{userid}/{filename}.json", "w") as f:
        f.write(contents)