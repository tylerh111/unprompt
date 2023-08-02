import io

import unprompt


def test_ask():
    with io.StringIO("i") as in_, io.StringIO("o") as out:
        ans = unprompt.ask(
            prompt="x",
            seperator="",
            in_=in_,
            out=out,
        )

        assert "i" == in_.getvalue()
        assert "x" == out.getvalue()
        assert ans == in_.getvalue()


def test_ask_with_newlines():
    with io.StringIO("i\n") as in_, io.StringIO("o\n") as out:
        ans = unprompt.ask(
            prompt="x\n",
            seperator="",
            in_=in_,
            out=out,
        )

        assert "i\n" == in_.getvalue()
        assert "x\n" == out.getvalue()
        assert ans == in_.getvalue()


def test_ask_separator():
    with io.StringIO("i") as in_, io.StringIO("o") as out:
        ans = unprompt.ask(
            prompt="x",
            seperator="\t",
            in_=in_,
            out=out,
        )

        assert "i" == in_.getvalue()
        assert "x\t" == out.getvalue()
        assert ans == in_.getvalue()
