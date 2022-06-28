from groups import *
from factors import naive_factorization


def test_get_multiplicative_elements():
    elems = get_multiplicative_elements(21)
    assert [1, 2, 4, 5, 8, 10, 11, 13, 16, 17, 19, 20] == elems
    elems = get_multiplicative_elements(36)
    assert [1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35] == elems


def test_compute_cycle():
    elems = compute_cycle(7, 8)
    assert [7, 1] == elems
    elems = compute_cycle(3, 10)
    assert [3, 9, 7, 1] == elems


def test_find_primitive_roots():
    roots = find_primitive_roots(19)
    assert [2, 3, 10, 13, 14, 15] == roots


def test_is_primitive_root():
    assert not is_primitive_root(5, 19, [2, 3])
    assert is_primitive_root(10, 19, [2, 3])
    assert is_primitive_root(3374359722, 8661340973, [2, 4])


def test_find_primitive_root():
    p = 8661340973
    f = naive_factorization(p-1)
    root = find_primitive_root(p, prime_factors=f)
    assert is_primitive_root(root, p, f)
