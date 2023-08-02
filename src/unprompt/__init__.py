"""
Unprompt - The User iNquiry Prompt
"""

from unprompt.prompt import ask

try:
    from unprompt._version import version as __version__  # noqa: F401
except ModuleNotFoundError:
    __version__ = "0.0"
