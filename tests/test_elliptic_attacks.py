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


def test_pohlig_hellman():
    ec = EllipticCurve(1001, 75, 7919)
    order = 7889
    p = (4023, 6036)
    assert ec.is_valid_point(p)
    assert ec.multiply(p, order) is None

    q = (4135, 3169)
    factors = [7**3, 23]
    p0 = ec.multiply(p, order // 23)
    print(p0)
    q0 = ec.multiply(q, order // 23)
    print(q0)
    l2 = naive_prime_attack(ec, p0, 23, q0)
    assert l2 == 10
    # TODO: finish example