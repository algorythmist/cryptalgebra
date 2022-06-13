import pytest

from integers import *


def test_gcd():
    assert 64 == gcd(128, 64)
    assert 33 == gcd(66, 99)
    assert 2 == gcd(1180, 482)
    g = gcd(8765, 23485)
    assert 5 == g
    assert 8765 % g == 0
    assert 23485 % g == 0


def test_gcd_invalid_arguments():
    with pytest.raises(AssertionError) as error:
        gcd(-10, 21)
    assert 'Arguments must be non-negative integers' == error.value.args[0]


def test_lcm():
    assert 33 == lcm(11, 33)
    assert 66 == lcm(6, 33)


def test_extended_euclidean_algorithm():
    x, y = extended_euclidean_algorithm(1180, 482)
    assert -29 == x
    assert 71 == y
    assert 2 == x * 1180 + y * 482

    x, y = extended_euclidean_algorithm(482, 1180)
    assert 71 == x
    assert -29 == y
    assert 2 == x * 482 + y * 1180


def test_mod_inverse():
    assert 9 == mod_inverse(5, 11)
    assert 5 == mod_inverse(9, 11)
    assert 6 == mod_inverse(2, 11)


def test_mod_solve():
    s = mod_solve(12, 21, 39)
    assert [5, 18, 31] == s


def test_mod_power():
    p = mod_power(2, 1234, 789)
    assert 481 == p