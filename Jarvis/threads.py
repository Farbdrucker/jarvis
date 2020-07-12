import concurrent.futures
import sys
import time
from typing import Callable

import Jarvis.log as logging


def threading(fun: Callable, *args, **kwargs):
    """
    runs provided function in a thread with provided arguments
    while displaying a rotation processing animation
    Args:
        fun: function to call
        *args: arguments
        **kwargs: key word arguments

    Returns:
        output of provided function
    """
    # global stop thread var, perform wait animation until `fun` is finished
    global stop_threads
    stop_threads = False

    def finishable_task(f, *a, **ka):
        global stop_threads
        try:
            out = f(*a, **ka)
        except Exception as e:
            logging.warning(str(e))
            out = None
        stop_threads = True
        return out

    def wait_animation(loading_speed=4):
        loading_string = ['|', '/', '-', '\\']

        while True:
            #  track both the current character and its index for easier backtracking later
            for index, char in enumerate(loading_string):
                # you can check your loading status here
                # if the loading is done set `loading` to false and break
                sys.stdout.write(char)  # write the next char to STDOUT
                sys.stdout.flush()  # flush the output
                time.sleep(1.0 / loading_speed)  # wait to match our speed
                sys.stdout.write("\b")
            global stop_threads
            if stop_threads:
                sys.stdout.write("\b")
                break

    executer = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    animate = executer.submit(wait_animation)
    f = executer.submit(finishable_task, fun, *args, **kwargs)

    return f.result()


def my_threading(func: Callable):
    """
    my threading decorator, runs provived function with `args` and `kwargs` in a thread
    while displaying a rotating processing animation
    """
    def wrapper_thread(*args, **kwargs):
        return threading(func, *args, **kwargs)

    return wrapper_thread

