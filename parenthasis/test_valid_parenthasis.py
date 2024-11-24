import pytest

from valid_parenthasis import isValid

@pytest.mark.parametrize(
    "input, expected",
    [
        ("()", True),
        ("(){}[]", True),
        ("[({})]", True),
        ("{[}]", False)
    ]
)
def test_longest_prefix(input, expected):
    assert isValid(input) == expected