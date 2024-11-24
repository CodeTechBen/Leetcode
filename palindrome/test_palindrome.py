import pytest

from two_point_palindrome import isPalindrome

@pytest.mark.parametrize(
    "input, expected",
    [
        ("racecar", True),
        ("abba", True),
        ("abbcbba", True),
        ("qwerty", False),
        ("a", True),
        ("ab", False),
    ]
)
def test_is_palindrome(input, expected):
    assert isPalindrome(input) == expected