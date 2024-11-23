import pytest

from oneliner import romanToInt

@pytest.mark.parametrize(
    "roman, expected",
    [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("XXI", 21),
        ("XC", 90),
        ("CD", 400),
        ("MMXXIV", 2024),
        ("MDCLXVI", 1666),
        ("I", 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000)
    ]
)
def test_roman_to_int(roman, expected):
    assert romanToInt(roman) == expected