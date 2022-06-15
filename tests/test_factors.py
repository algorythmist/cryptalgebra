from factors import *


def test_naive_factorization():
    assert len(naive_factorization(19)) == 0
    assert [2, 3] == naive_factorization(18)
    assert [2, 4, 7, 8, 14, 28, 56] == naive_factorization(9688)


def test_find_primes():
    primes = find_primes(1000)
    assert 168 == len(primes)


def test_is_square():
    assert not is_square(10)
    assert is_square(100)


def test_fermat_factorization():
    p = 28559
    q = 95177
    p_found, q_found = fermat_factorization(p*q)
    assert p == p_found
    assert q == q_found
