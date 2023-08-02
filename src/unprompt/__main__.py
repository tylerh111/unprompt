import sys

import click

from . import __version__, ask


@click.command(
    options_metavar="<options>",
    help="User iNquiry Prompt",
)
@click.help_option(
    "-h",
    "--help",
)
@click.version_option(
    __version__,
    "-v",
    "--version",
    message="%(prog)s %(version)s",
    is_eager=True,
)
@click.option(
    "-d",
    "--default",
    nargs=1,
    default=None,
    metavar="<default>",
)
@click.argument(
    "prompt",
    nargs=1,
    type=str,
    metavar="<prompt>",
    # help='Prompt to ask the user.',
)
def main(
    prompt,
    default,
):
    """Asks user for input and prints it to stdout.

    :param prompt: The prompt to show to the user.
    :param default: The default value used if the user enters nothing. (Default: None)

    """
    res = ask(prompt, default)
    print(res)


if __name__ == "__main__":
    sys.exit(main())
