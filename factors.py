"""
Algorithms for finding the factorization of integers
"""

import math
from math import isqrt

from bitarray import bitarray

from integers import mod_power, gcd


def find_primes(upto=100):
    """
    Find all primes up to n using the Sieve of Eratosthenes
    :param upto: find all primes up to this number
    :return: the list of primes
    """
    is_prime = bitarray(upto)
    is_prime.setall(False)
    is_prime[3::2] = True

    is_prime[2] = True
    for candidate in range(3, isqrt(upto) + 1, 2):
        if is_prime[candidate]:
            is_prime[candidate * candidate::2 * candidate] = False

    return [n for n in range(2, upto) if is_prime[n]]


def tree_factorization(n: int) -> list[tuple[int, int]]:
    """
    Factor an integer using the tree method
    :param n: the integer to factor
    :return: a list with the factors
    """

    def find_multiplicity(factor: int, number) -> int:
        count = 0
        while number % factor == 0:
            count += 1
            number //= factor
        return count

    factors = []
    for f in range(2, n):
        if n % f == 0:
            m = find_multiplicity(f, n)
            factors.append((f, m))
            n //= f ** m
        if n == 1:
            break
    return factors


def naive_factorization(n: int) -> list[int]:
    """
    TODO: This will not return multiplicity of each factor and may return powers of a factor
    Example:naive_factorization(7889) returns [7, 23, 49]
    """
    sq = int(math.ceil(math.sqrt(n)))
    return [f for f in range(2, sq) if n % f == 0]


def fermat_factorization(n: int, max_tries=1000000) -> tuple[int, int]:
    for k in range(1, max_tries):
        x = n + k ** 2
        if is_square(x):
            sx = math.isqrt(x)
            return sx - k, sx + k
    raise ValueError("Could not factor")


def factorial_power(a: int, bound: int, n: int):
    """
    Compute a ** bound! mod n
    :param a:
    :param n:
    :param bound:
    :return:
    """
    b = a
    for k in range(2, bound + 1):
        b = mod_power(b, k, n)
    return b


def factorial_factoring(n: int, base: int = 2, bound=30) -> int:
    """
    Attempt to factor an integer by computing the factorial powers:
    (p-1) factoring method
    :param n: the integer to factor
    :param base: a base for computing the factorial power mod n
    :param bound: the factoring power to compute
    :return: A factor if one is found, or 1 if it is not
    """
    b = factorial_power(base, bound, n)
    return gcd(b - 1, n)


def pollard_rho_factorization(n: int, x: int = 2, c: int = 1, iterations: int = 10000) -> int:
    """
    Pollard's rho algorithm for factoring
    :param n: the integer to factor
    :param x: the starting point
    :param c: the constant
    :param iterations: the number of iterations
    :return: a factor if one is found
    """
    f = lambda x: (x ** 2 + c) % n
    y = x
    for _ in range(iterations):
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
        if d != 1:
            return d
    raise ValueError("No factor found")


def is_square(n: int) -> bool:
    return math.isqrt(n) ** 2 == n
