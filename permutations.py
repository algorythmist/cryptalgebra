import itertools
from ctypes import Array


class Permutation:

    def __init__(self, permutationArray: Array[int]):
        if not is_valid_permutation(permutationArray):
            raise ValueError("The given array is not a valid permutation")
        self._permutation_array = permutationArray

    @staticmethod
    def create(*indices):
        return Permutation(list(indices))

    @staticmethod
    def cycle(cycle: Array[int], size: int):
        perm = identity(size)
        cycle_size = len(cycle)
        perm[cycle[cycle_size - 1]] = cycle[0]
        for i in range(cycle_size - 1):
            perm[cycle[i]] = cycle[i + 1]
        return Permutation(perm)

    @staticmethod
    def transposition(t, size):
        perm = identity(size)
        swap(perm, t[0], t[1])
        return Permutation(perm)

    def __len__(self):
        return len(self._permutation_array)

    def __str__(self):
        return str(self._permutation_array)

    def __repr__(self):
        return str(self._permutation_array)

    def __getitem__(self, key):
        return self._permutation_array[key]

    def __mul__(self, other):
        return Permutation(compose(self._permutation_array, other._permutation_array))

    def to_array(self):
        return self._permutation_array.copy()

    def to_matrix(self):
        size = len(self._permutation_array)
        matrix = [[0] * size for _ in range(size)]
        for i in range(size):
            matrix[i][self[i]] = 1
        return matrix

    def fixes(self) -> set[int]:
        return set(i for i in range(len(self)) if self[i] == i)


def is_valid_permutation(permutationArray: Array[int]) -> bool:
    """
    Checks if the given array is a valid permutation
    :param permutationArray: the array to check
    :return: True if the array is a valid permutation, False otherwise
    """
    if len(permutationArray) == 0:
        return False
    permutationSet = set(permutationArray)
    for i in permutationArray:
        if i < 0 or i >= len(permutationArray):
            return False
        permutationSet.add(i)
    return len(permutationSet) == len(permutationArray)


def inverse(permutation: Array[int]) -> Array[int]:
    """
    Computes the inverse of a permutation
    :param permutation_array: the permutation to invert
    :return: the inverse of the permutation
    """
    inverse = [0] * len(permutation)
    for i in range(len(permutation)):
        inverse[permutation[i]] = i
    return inverse


def compose(permutation1: Array[int], permutation2: Array[int]) -> Array[int]:
    """
    Composes two permutations
    :param permutation1: the first permutation
    :param permutation2: the second permutation
    :return: the composition of the two permutations
    """
    if len(permutation1) != len(permutation2):
        raise ValueError("Permutations must be of the same length")
    return [permutation1[permutation2[i]] for i in range(len(permutation1))]


def identity(size):
    return [i for i in range(size)]


def swap(permutation, a, b):
    permutation[a] += permutation[b]
    permutation[b] = permutation[a] - permutation[b]
    permutation[a] -= permutation[b]


def reverse(permutation, point1, point2):
    """
    Reverse the sub-permutation specified by two indices.

    Args:
        permutation (List[int]): The starting permutation.
        point1 (int): The index where the reversal starts (inclusive).
        point2 (int): The index where the reversal ends (exclusive).
    """
    size = len(permutation)
    swaped = (point2 - point1 + size + 1) % (size + 1) // 2

    j = 0
    while j < swaped:
        k = (point1 + j) % size
        l = (point2 - j - 1 + size) % size
        swap(permutation, k, l)
        j += 1


def iterate_permutations(size):
    elements = list(range(size))
    for permutation in itertools.permutations(elements):
        yield permutation
