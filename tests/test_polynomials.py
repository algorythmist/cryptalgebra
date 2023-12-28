from polynomials import Polynomial


def test_create():
    p = Polynomial(1, 2, 3, 0, 0, 0)
    assert p.coefficients == (1, 2, 3)
    assert p == Polynomial(1, 2, 3)


def test_evaluate():
    p = Polynomial(1, 2, 3)
    assert p.evaluate(0) == 1
    assert p.evaluate(1) == 6
    assert p.evaluate(2) == 17


def test_order():
    p1 = Polynomial(1, 2, 3)
    assert p1.order() == 2
    p2 = Polynomial(3, 4, 5, 6)
    assert p2.order() == 3


def test_add():
    p1 = Polynomial(1, 2, 3)
    p2 = Polynomial(3, 4, 5, 6)
    p3 = p1 + p2
    assert p3.coefficients == (4, 6, 8, 6)
    assert p3 == p2 + p1


def test_subtract():
    p1 = Polynomial(1, 2, 3)
    p2 = Polynomial(3, 4, 0, 6)
    p3 = p1 - p2
    assert p3.coefficients == (-2, -2, 3, -6)
    p4 = p2 - p1
    assert p4.coefficients == (2, 2, -3, 6)


def test_repr():
    p1 = Polynomial(1, 2, 3)
    assert repr(p1) == '1 + 2x + 3x^2'

    p2 = Polynomial(1, 0, 3)
    assert repr(p2) == '1 + 3x^2'

    p3 = Polynomial(1, 0, 0)
    assert repr(p3) == '1'

    p4 = Polynomial(0, 0, 1)
    assert repr(p4) == 'x^2'

    p5 = Polynomial(0, 1, 1)
    assert repr(p5) == 'x + x^2'


def test_multiply():
    p1 = Polynomial(1, 2, 3)
    p2 = Polynomial(3, 4, 0, 6)
    p3 = p1 * p2
    assert p3.coefficients == (3, 10, 17, 18, 12, 18)
    assert p3 == p2 * p1


