import pytest

from main import light_bulbs

@pytest.mark.parametrize(
    "lights, n, expected",
    [
        ([0, 1, 1, 0, 1, 1], 2, [1, 0, 1, 1, 0, 1]),
        ([1, 0, 1, 1, 0, 1, 1, 0, 1], 10,  [0, 1, 1, 0, 1, 1, 0, 1, 1]),
        ([1, 1, 0, 0, 0, 1, 1, 1, 1, 1], 20,  [1, 0, 0, 0, 0, 0, 1, 1, 0, 1]),
    ]
)

def test_light_bulbs(lights, n, expected):
    assert light_bulbs(lights, n) == expected
