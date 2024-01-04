from polynomials import Polynomial


def test_create():
    p = Polynomial(1, 2, 3, 0, 0, 0)
    assert p.coefficients == (1, 2, 3)
    assert p == Polynomial(1, 2, 3)


def test_evaluate():
    p = Polynomial(1, 2, 3)
    assert p(0) == 1
    assert p.evaluate(1) == 6
    assert p(2) == 17


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


def test_is_monomial():
    # Test 1
    m1 = Polynomial.monomial(10, 8)
    assert m1.is_monomial()

    # Test 2
    m2 = Polynomial.monomial(5, 2)
    assert m2.is_monomial()

    # Test 3
    p = m1 + m2
    assert not p.is_monomial()


def test_monomial_power():
    # Creating a monomial polynomial
    m = Polynomial.monomial(2, 2)
    assert m.degree == 2  # Checking the degree of the monomial

    # Raising the monomial polynomial to the power of 5
    m5 = m ** (5)

    # Assertions
    assert m.is_monomial()
    assert m5.degree == 10
    assert str(m5) == "2x^10"


def test_power():
    # Creating a non-monomial polynomial
    p = Polynomial(1, 2, 2)

    # Raising the polynomial to the power of 5
    p3 = p**3
    assert '1 + 6x + 18x^2 + 32x^3 + 36x^4 + 24x^5 + 8x^6' == str(p3)
