import pytest

from long_prefix import longestCommonPrefix

@pytest.mark.parametrize(
    "input, expected",
    [
        (["flower","flow","flight"], "fl"),
        (["dog","racecar","car"], ""),
        (["ap","apple","apostraphy"], "ap"),
    ]
)
def test_longest_prefix(input, expected):
    assert longestCommonPrefix(input) == expected