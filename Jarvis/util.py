from datetime import datetime


def argmax(list_):
    return max(enumerate(list_), key=lambda x: x[1])[0]


def now():
    return str(datetime.now())