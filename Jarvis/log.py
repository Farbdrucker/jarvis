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


class logging:
    @staticmethod
    def prep(func):
        return f"{now()} {func}: ".upper()

    @staticmethod
    def pprint(args):
        print(args + color.END)

    @staticmethod
    def info(args):
        logging.pprint(logging.prep("info") + args)

    @staticmethod
    def warning(args):
        logging.pprint(color.BOLD + color.RED + logging.prep("warning") + args)

    @staticmethod
    def msg(args):
        logging.pprint(color.BOLD + logging.prep("message") + args)

    @staticmethod
    def jarvis(args):
        logging.pprint(color.BOLD + color.CYAN + logging.prep("jarvis") + args)

    @staticmethod
    def understood(args):
        logging.pprint(color.BOLD + color.YELLOW + logging.prep("input") + args)

    @staticmethod
    def debug(args):
        logging.pprint(logging.prep("debug") + args)
