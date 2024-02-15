from elliptic import EllipticCurve
from integers import mod_inverse


def test_elliptic_curve():
    ec = EllipticCurve(4, 20, 29)
    assert str(ec) == "y^2 = x^3 + 4x + 20 (mod 29)"
    assert ec.determinant() == 4
    assert ec.is_valid_point((5, 22))
    assert ec.is_valid_point((15, 27))

    result = ec.add((5, 22), (16, 27))
    assert result == (13, 6)

    result = ec.double((5, 22))
    assert result == (14, 6)

    assert ec.negate((5, 22)) == (5, 7)


def test_infinity():
    ec = EllipticCurve(4, 20, 29)

    assert ec.add((1, 5), (1, 24)) is None
    assert ec.add((5, 22), None) == (5, 22)
    assert ec.add(None, (5, 22)) == (5, 22)
    assert ec.add(None, None) is None
    assert ec.double(None) is None
    assert ec.negate(None) is None


def test_multiply():
    ec = EllipticCurve(4, 20, 29)
    p = (1, 5)
    assert ec.is_valid_point(p)
    assert ec.multiply(p, 2) == (4, 19)
    assert ec.multiply(p, 21) == (0, 7)
    assert ec.multiply(p, 0) is None
    assert ec.multiply(p, 37) is None


def test_pohlig_hellman():
    ec = EllipticCurve(1001, 75, 7919)
    order = 7889
    p = (4023, 6036)
    assert ec.is_valid_point(p)
    assert ec.multiply(p, order) is None
    # TODO: finish example

