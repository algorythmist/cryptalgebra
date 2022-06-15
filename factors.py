import math

from bitarray import bitarray
from math import isqrt


def find_primes(upto=100):
    """
    Find all primes up to n using the Sieve of Erathosthenes
    :param upto: find all primes up to this number
    :return: the list of primes
    """
    is_prime = bitarray(upto)
    is_prime.setall(False)
    is_prime[3::2] = True

    is_prime[2] = True
    for candidate in range(3, isqrt(upto) + 1, 2):
        if is_prime[candidate]:
            is_prime[candidate*candidate::2*candidate] = False

    return [n for n in range(2, upto) if is_prime[n]]


def naive_factorization(n: int) -> list:
    sq = int(math.ceil(math.sqrt(n)))
    return [f for f in range(2, sq) if n % f == 0]


def is_square(n: int) -> bool:
    return math.isqrt(n)**2 == n


def fermat_factorization(n:int, max_tries=1000000):
    for k in range(1, max_tries):
        x = n+k**2
        if is_square(x):
            sx = math.isqrt(x)
            return sx-k, sx+k
    raise ValueError("Could not factor")

