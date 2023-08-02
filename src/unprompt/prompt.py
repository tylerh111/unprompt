import sys
from typing import Optional, TextIO


def ask(
    prompt: str,
    default: Optional[str] = None,
    *,
    seperator: str = " ",
    in_: TextIO = sys.stdin,
    out: TextIO = sys.stdout,
) -> str:
    """
    Asks user for input and return it.

    :param prompt: The prompt to show to the user.
    :param default: The default value used if the user enters nothing. (Default: ``None``)
    :param seperator: Separator between prompt and user's text.  (Default: single space)
    :param in_: Input IO object to read from. (Default: ``sys.stdin``)
    :param out: Output IO object to write to. (Default: ``sys.stdout``)

    """
    prompt = prompt + seperator
    print(prompt, file=out, end="")
    answer = in_.readline()
    return answer or default
