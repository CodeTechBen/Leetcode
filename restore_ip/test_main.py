"""tests main file solution"""
import pytest
from main import validate_string, validate_segment, combine_segments, iterate_string


@pytest.mark.parametrize(
    "input, expected",
    [
        ("192168@11", False),
        ("012201", True),
        ("1", False),
        ("1111111111111", False),
    ]
)
def test_validate_string_base_test(input, expected):
    assert validate_string(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ('hello', False),
        (['123456', '23456'], False),
        (234567, False)
    ]
)
def test_validate_string_edge(input, expected):
    assert validate_string(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ('256', False),
        ('0', True),
        ('00', False),
        ('255', True)
    ]
)
def test_validate_segment(input, expected):
    assert validate_segment(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (['123', '123', '123', '123'], '123.123.123.123')
    ]
)
def test_combine_segments(input, expected):
    assert combine_segments(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ('25525511135', ["255.255.11.135", "255.255.111.35"]),
        ("0000", ["0.0.0.0"]),
        ("101023", ["1.0.10.23", "1.0.102.3",
        "10.1.0.23", "10.10.2.3", "101.0.2.3"])
    ]
)
def test_iterate_string(input, expected):
    assert iterate_string(input) == expected
