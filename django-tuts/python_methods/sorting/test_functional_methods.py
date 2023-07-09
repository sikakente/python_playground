import unittest

import pytest

from .functional import power_of_5


@pytest.mark.parametrize("num,expected", [
    (2, 32),
    (0, 0)
])
def test_power_of(num, expected):
    assert expected == power_of_5(num)


if __name__ == '__main__':
    unittest.main()
