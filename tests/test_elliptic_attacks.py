from elliptic import EllipticCurve
from elliptic_attacks import naive_prime_attack


def test_naive_prime():
    ec = EllipticCurve(1, 44, 229)
    order = 239
    p = (5, 116)
    assert ec.is_valid_point(p)
    assert ec.multiply(p, order) is None
    q = (155, 166)
    l = naive_prime_attack(ec, p, order, q)
    assert l == 176
    assert q == ec.multiply(p, l)