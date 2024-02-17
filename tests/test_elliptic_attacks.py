from elliptic import EllipticCurve
from elliptic_attacks import naive_prime_attack, PohlighHellman
from integers import solve_chinese_remainder


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
    p0 = ec.multiply(p, order // 23)
    q0 = ec.multiply(q, order // 23)
    l2 = naive_prime_attack(ec, p0, 23, q0)
    assert l2 == 10

    ph = PohlighHellman(ec, p, order, q)
    l1 = ph._determine_prime_representation(23, 1)
    assert l1 == 10
    l2 = ph._determine_prime_representation(7, 3)
    assert l2 == 218
    l = solve_chinese_remainder([(l1, 23), (l2, 7 ** 3)])
    assert l == 4334

    assert ph.solve() == 4334
    assert q == ec.multiply(p, 4334)
