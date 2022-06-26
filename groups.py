from integers import gcd, mod_power
import random


def get_multiplicative_elements(n: int) -> list:
    """
    Compute all elements of the multiplicative group U(n)
    :param n:
    :return:
    """
    return [k for k in range(1, n) if gcd(k, n) == 1]


def compute_cycle(a, n):
    """
    Compute <a> in U(n)
    :param a:
    :param n:
    :return:
    """
    if a > n:
        a = a % n
    elems = [a]
    product = a
    for i in range(2, n):
        if product == 1:
            return elems
        product = a*product % n
        elems.append(product)
    return elems


def find_primitive_roots(p: int) -> list:
    """
    Naive and slow way for primitive roots
    :param p:
    :return:
    """
    return [a for a in range(2, p) if len(compute_cycle(a, p)) == p-1]


def is_primitive_root(g: int, prime: int, prime_factors: list) -> bool:
    """
    Determine if n is a primitive root of a prime, given the prime factors of p-1
    :param g: the potential root in question
    :param prime: the prime number whose root we seek
    :param prime_factors: the prime factors of the integer prime-1
    :return:
    """
    n = prime-1
    for factor in prime_factors:
        if mod_power(g, n/factor, prime) == 1:
            return False
    return True


def find_primitive_root(prime: int, prime_factors: list,
                        attempts = 1000) -> int:
    """
    Attempts to find a primitive root of a prime number p, if the factorization of p-1 is known
    :param prime: the prime number
    :param prime_factors: the prime factors of prime-1
    :param attempts: number of times to try
    :return: a primitive root if found
    :raises ValueError if no roots were found
    """
    attempted = set()
    for _ in range(attempts):
        g = random.randint(2, prime-1)
        if g in attempted:
            continue
        if is_primitive_root(g, prime, prime_factors):
            return g
        else:
            attempted.add(g)
    raise ValueError("Could not find a primitive root")
