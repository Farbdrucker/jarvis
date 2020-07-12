from typing import Tuple, Type

from .commands import *
from ..util import argmax


def know_command(msg: str) -> Tuple[bool, Type[Command]]:
    """
    checks and compare input `msg` to defined commands
    Args:
        msg: input message as str

    Returns:
        tuple of bool (True if a known command was derived) and the predicted `Command`
    """
    split_msg = msg.lower().split(' ')

    my_commands = [WikiSearch, Joke, ShowWeather, HowAreYou, WhatIsTheAnswer, RoayalWithCheesee, FuckYouToo]

    most_likely_answer = []
    for command in my_commands:
        checked_tokens = [t.lower() in split_msg for t in command.tokens()]
        if all(checked_tokens):
            return True, command
        else:
            most_likely_answer.append(sum(checked_tokens))

    index = argmax(most_likely_answer)
    return True, my_commands[index]


def commands(msg: str) -> str:
    """
    looks for implemented `Command`s based on the input message and executes it
    Args:
        msg: message

    Returns:
        out put of predicted `Command`
    """
    try:
        known_command, command = know_command(msg)

        if command is not None and known_command:
            logging.info(f"applying \"{msg}\" on {command}")
            return command.action(msg)
        else:
            logging.warning(f"command unknown: {msg}")
            return 'Sorry I do not know what to do.'

    except Exception as e:
        logging.warning(str(e))
