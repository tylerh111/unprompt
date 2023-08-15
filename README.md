# Unprompt

[![Version](https://img.shields.io/badge/version-0.1-blue)](https://github.com/tylerh111/unprompt)
[![License](https://img.shields.io/badge/license-MIT-blueviolet)](https://github.com/tylerh111/unprompt/blob/main/LICENSE.md)

> Simply ask the user

*Unprompt* is the user inquiry prompt.
It provides a simple and elegant way of asking the user for input in interactive scripts and programs.

* **Source:** [https://github.com/tylerh111/unprompt](https://github.com/tylerh111/unprompt)
* **Documentation:** [https://unprompt.readthedocs.io](https://unprompt.readthedocs.io)

## Installation

*Unprompt* can be installed by running `pip install unprompt`.
To get the latest development version, use: `pip install git+https://github.com/tylerh111/unprompt`.

## Usage

*Unprompt* can be used as command or in your python code.
To ask the user for input on the command line, run the following command:
```bash
unprompt "How are you?"  # How are you? Great!
```

To ask the user for input on the command line, simply import the package and call the `ask` function.
```python
import unprompt
answer = unprompt.ask("How are you?")  # How are you? Great!
```
