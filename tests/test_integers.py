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
    assert 17 == mod_inverse(17, 24)
    assert 17 == mod_inverse(-7, 24)


def test_mod_solve():
    s = mod_solve(12, 21, 39)
    assert [5, 18, 31] == s


def test_mod_power():
    p = mod_power(2, 1234, 789)
    assert 481 == p
    p = mod_power(263, 2, 561)
    assert 166 == p


def test_remove_powers_of_2():
    n = 773
    k, m = remove_powers_of_2(n - 1)
    assert 2 == k
    assert 193 == m

    n = 561
    k, m = remove_powers_of_2(n - 1)
    assert 4 == k
    assert 35 == m


def test_is_probably_prime():
    assert not is_probably_prime(561)
    assert not is_probably_prime(667)
    assert is_probably_prime(773)
    assert is_probably_prime(983)
    assert is_probably_prime(173530588845534154720930373401)
    n = 38200901201  # This is a strong pseudo prime, so a single M-R test may fail
    assert not is_probably_prime(n)


def test_random_number():
    n = random_number(10)
    assert 10 == len(str(n))
    n = random_number(47)
    assert 47 == len(str(n))


def test_generate_random_prime():
    prime = generate_random_prime(100)
    assert 100 == len(str(prime))


def test_chinese_remainder_1():
    remainders = [(2, 5), (3, 7), (10, 11)]
    x = solve_chinese_remainder(remainders)
    assert 87 == x
    for a, m in remainders:
        assert x % m == a


def test_chinese_remainder_2():
    remainders = [(6, 11), (13, 16), (9, 21), (19, 25)]
    x = solve_chinese_remainder(remainders)
    assert 89469 == x
    for a, m in remainders:
        assert x % m == a
