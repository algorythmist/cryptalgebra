from elliptic import EllipticCurve


def test_elliptic_curve():
    ec = EllipticCurve(4, 20, 29)
    assert str(ec) == "y^2 = x^3 + 4x + 20 (mod 29)"
    assert ec.determinant() == 4
    assert ec.is_valid_point(5, 22)
    assert ec.is_valid_point(15, 27)

    result = ec.add((5, 22), (16, 27))
    assert result == (13, 6)

    result = ec.double((5, 22))
    assert result == (14, 6)

    assert ec.negate((5, 22)) == (5, 7)
