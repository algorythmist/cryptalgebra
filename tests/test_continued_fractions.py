import math

import pytest

from continued_fractions import *


def test_greater_than_one():
    l1 = compute_continued_fraction(52, 9)
    assert [5, 1, 3, 2] == l1
    l2 = compute_continued_fraction(13, 8)
    assert [1, 1, 1, 1, 2] == l2


def test_less_than_one():
    l1 = compute_continued_fraction(5, 8)
    assert [0, 1, 1, 1, 2] == l1
    l2 = compute_continued_fraction(7, 9)
    assert [0, 1, 3, 2] == l2


def test_one_over():
    l = compute_continued_fraction(1, 9)
    assert [0, 9] == l


def test_zero_numerator():
    assert [0] == compute_continued_fraction(0, 2)


def test_zero_denominator():
    with pytest.raises(ValueError) as ve:
        compute_continued_fraction(2, 0)
    assert str(ve.value) == "Denominator should not be 0"


def test_non_integers():
    assert compute_continued_fraction(5, 3) == compute_continued_fraction(5.2, 3.8)


def test_unreduced():
    l1 = compute_continued_fraction(2, 4)
    assert [0, 2] == l1
    l2 = compute_continued_fraction(9, 6)
    assert [1, 2] == l2


def test_continued_fraction_from_real():
    real = math.sqrt(2)
    result = _verify_precision(real, 15)
    assert [1] + [2] * 20 == result[:21]
    real = 7 - 3 ** (1 / 2)
    result = _verify_precision(real, 15)
    assert [5, 3] + [1, 2] * 10 == result[:22]
    result = _verify_precision(math.pi, 15)
    expected = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1]
    assert expected[:13] == result[:13]


def test_restore():
    assert 52 / 9 == restore([5, 1, 3, 2])
    assert 13 / 8 == restore([1, 1, 1, 1, 2])
    assert 0.5 == restore([0, 2])


def test_find_convergent():
    expansion1 = compute_continued_fraction(19, 17)
    assert [1, 8, 2] == expansion1
    c1 = find_convergent(expansion1)
    assert (19, 17) == c1

    expansion2 = compute_continued_fraction(77, 65)
    assert [1, 5, 2, 2, 2] == expansion2
    c2 = find_convergent(expansion2)
    assert (77, 65) == c2


def _verify_precision(real, precision):
    result = continued_fraction_from_real(real, precision)
    restored = restore(result)
    assert math.isclose(real, restored, rel_tol=10 ** -precision)
    return result
