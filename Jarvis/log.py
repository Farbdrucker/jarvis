from Jarvis.util import now


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def pprint(func):
    def wrapper(msg):
        c = func(msg)
        print(f"{c}{now()} {str(func.__name__).upper()}: {msg}{color.END}")

    return wrapper


@pprint
def info(args):
    return ''


@pprint
def warning(args):
    return color.BOLD + color.RED


@pprint
def msg(args):
    return color.BOLD


@pprint
def jarvis(args):
    return color.BOLD + color.CYAN


@pprint
def understood(args):
    return color.BOLD + color.YELLOW


@pprint
def debug(args):
    return ''

