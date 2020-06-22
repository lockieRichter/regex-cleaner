import pytest

from .regex_cleaner.regex_cleaner import clean_regex


@pytest.mark.parametrize(
    "verbose_pattern, expected",
    [
        (
            r"""
            ^ # Start of line.
            \w # Match any word.
            $ # End of line.
            """,
            r"^\w$",
        ),
        (r"^\w$", r"^\w$"),
        (
            r"""
            ^ # Start of a line.
            (?: # Non capture group: user-name-character
                [a-zA-Z0-9_+-]+ # Any letter, number or -,+,_ symbol, one or more times.
                \.? # Zero or one optional periods.
            )+ # Repeat group user-name-character one or more times.
            @ # A single @ sign.
            [a-zA-Z0-9]+ # Any lettter or number. (Domain name).
            \. # A single period.
            [a-zA-Z0-9-]+ # Any letter, number or a dash. (Domain extension).
            \.? # Zero or one period.
            [a-zA-Z0-9-]+ # One or more letters, numbers or dash. (Optional domain extension).
            $ # End of a line.
            """,
            r"^(?:[a-zA-Z0-9_+-]+\.?)+@[a-zA-Z0-9]+\.[a-zA-Z0-9-]+\.?[a-zA-Z0-9-]+$",
        ),
    ],
)
def test_get_entity(verbose_pattern, expected):
    assert clean_regex(verbose_pattern) == expected
