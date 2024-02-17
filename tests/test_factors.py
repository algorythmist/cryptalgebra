from factors import *


def test_naive_factorization():
    assert len(naive_factorization(19)) == 0
    assert [2, 3] == naive_factorization(18)
    assert [2, 4, 7, 8, 14, 28, 56] == naive_factorization(9688)


def test_tree_factorization():
    assert tree_factorization(2048) == [(2, 11)]
    assert tree_factorization(18) == [(2, 1), (3, 2)]
    assert tree_factorization(9688) == [(2, 3), (7, 1), (173, 1)]


def test_pollard_rho_factorization():
    n = 8661340972
    assert pollard_rho_factorization(n) == 4


def test_find_primes():
    primes = find_primes(1000)
    assert 168 == len(primes)


def test_is_square():
    assert not is_square(10)
    assert is_square(100)


def test_fermat_factorization():
    p = 28559
    q = 95177
    p_found, q_found = fermat_factorization(p * q)
    assert p == p_found
    assert q == q_found


def test_factorial_power():
    a = 2
    k = 4
    result = mod_power(a, 24, 19)
    assert 7 == result
    fp = factorial_power(a, k, 19)
    assert result == fp


def test_factorial_factoring():
    n = 618240007109027021
    factor = factorial_factoring(n)
    assert 250387201 == factor
