import pytest

from paldindrome import is_palindrome


@pytest.mark.parametrize(
    "input, expected",
    [
        (["racecar", "abba","qwerty"], ["racecar", "abba"])
    ]
)
def test_is_palindrome_base_case(input, expected):
    assert is_palindrome(input) == expected

@pytest.mark.parametrize(
    "input, expected",
    [
        (["Racecar", "aBbA", "qweRty"], ["racecar", "abba"])
    ]
)
def test_is_palindrome_upper_case(input, expected):
    assert is_palindrome(input) == expected

@pytest.mark.parametrize(
    "input, expected",
    [
        (["Race.car", "aB,bA", "qweRt?y"], ["racecar", "abba"])
    ]
)
def test_is_palindrome_punctuation(input, expected):
    assert is_palindrome(input) == expected
