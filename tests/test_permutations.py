from permutations import *


def test_invalid():
    with pytest.raises(ValueError):
        Permutation([1, 0, 3, 3])
    with pytest.raises(ValueError):
        Permutation([1, 0, 3, 5])


def test_times():
    print(Permutation([1, 2, 0, 4, 3]) * Permutation([2, 3, 4, 0, 1]))

    permutation1 = Permutation([1, 0, 3, 2])
    assert len(permutation1) == 4
    permutation2 = Permutation([2, 1, 0, 3])
    composite1 = permutation1 * permutation2
    assert composite1.to_array() == [3, 0, 1, 2]
    composite2 = permutation2 * permutation1
    assert composite2.to_array() == [1, 2, 3, 0]


def test_times_incompatible():
    permutation1 = Permutation([1, 0, 3, 2])
    permutation2 = Permutation([2, 1, 0, 3, 4])
    with pytest.raises(ValueError):
        permutation1 * permutation2


def test_cycle():
    perm = Permutation.cycle([1, 3, 5], 6)
    assert perm.to_array() == [0, 3, 2, 5, 4, 1]
    expected = [
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0]
    ]
    assert perm.to_matrix() == expected


def test_transposition():
    perm = Permutation.transposition((1, 3), 6)
    assert perm.to_array() == [0, 3, 2, 1, 4, 5]


def test_fixes():
    perm = Permutation.create(0, 2, 1, 5, 4, 3)
    assert perm.fixes() == {0, 4}


import pytest


@pytest.mark.parametrize("size, expected", [
    (5, [0, 1, 2, 3, 4]),
])
def test_identity(size, expected):
    assert identity(size) == expected


def test_swap():
    permutation = [1, 0, 3, 2]
    swap(permutation, 0, 2)
    assert permutation == [3, 0, 1, 2]


def test_compose():
    permutation1 = [2, 1, 0, 3]
    permutation2 = [1, 0, 3, 2]
    composite = compose(permutation1, permutation2)
    assert composite == [1, 2, 3, 0]


def test_inverse():
    permutation = [1, 3, 4, 2, 0]
    inv = inverse(permutation)
    assert inv == [4, 0, 3, 1, 2]
    # Verify that the composition with the inverse gives the identity permutation
    composite = compose(permutation, inv)
    assert composite == [0, 1, 2, 3, 4]


def test_reverse():
    permutation = [1, 3, 4, 2, 0, 5]
    reverse(permutation, 1, 4)
    assert permutation == [1, 2, 4, 3, 0, 5]


@pytest.mark.parametrize("permutation, expected", [
    ([1, 3, 4, 2, 0, 5], True),
    ([1, 3, 4, 2, 5], False),
    ([1, 3, 4, -2, 0, 5], False),
    ([1, 3, 4, 2, 0, 5, 2], False),
    ([0, 3, 2, 5, 4, 1], True),
])
def test_is_valid(permutation, expected):
    assert is_valid_permutation(permutation) == expected
