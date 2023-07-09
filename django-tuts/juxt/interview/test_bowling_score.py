import unittest

import pytest

from .bowling_scoring import get_score


@pytest.mark.parametrize("throws,expected", [
    ([1, 2, 3, 4, 5, 5], 20),
    ([5, 5, 4, 3, 2, 1], 24),
    ([10, 10, 10], 60),
    ([0, 0, 0], 0)
])
def test_test_bowling_score(throws, expected):
    assert expected == get_score(throws)


if __name__ == '__main__':
    unittest.main()
