"""
Number-theoretic operations on integers
"""

import random
import logging


def is_even(n):
    return n % 2 == 0


def gcd(n1: int, n2: int) -> int:
    """
    Compute the greatest common divisor of two integers
    :param n1: a non-negative integer
    :param n2: a non-negative integer
    :return: the greatest common divisor.
    """
    assert (n1 >= 0 and n2 >= 0), "Arguments must be non-negative integers"
    if n1 < n2:
        return gcd(n2, n1)
    return n1 if n2 == 0 else gcd(n2, n1 % n2)


def lcm(n1: int, n2: int) -> int:
    """
    Compute the least common multiple
    :param n1: a non-negative integer
    :param n2: a non-negative integer
    :return: the least common multiple
    """
    return n1 * n2 / gcd(n1, n2)


def extended_euclidean_algorithm(n1: int, n2: int) -> (int, int):
    """
    Given n1, n2, compute x and y such that x*n1+y*n2 = gcd(n1, n2)
    :param n1: A positive integer
    :param n2: A positive integer
    :return: The pair (x, y)
    """
    assert n1 > 0 and n2 > 0, "Arguments must be positive integers"
    if n1 < n2:
        x, y = extended_euclidean_algorithm(n2, n1)
        return y, x
    quotient, remainder = n1 // n2, n1 % n2
    x0 = 0
    x1 = 1
    y0 = 1
    y1 = 0
    while remainder > 0:
        x0, x1 = x1, -quotient * x1 + x0
        y0, y1 = y1, -quotient * y1 + y0
        n1, n2 = n2, remainder
        quotient, remainder = n1 // n2, n1 % n2
    return y1, x1


def mod_inverse(a, m):
    """
    Compute the multiplicative inverse of a mod m.
    It is required that gcd(a,n) = 1
    :param a: the integer
    :param m: the modulo
    :return: the multiplicative inverse of a mod m
    """
    assert m > 0, "Modulo must be a positive integer"
    if a < 0:
        a = m + a
    assert gcd(m, a) == 1, "The integers must be relatively prime"
    x, y = extended_euclidean_algorithm(m, a)
    return y if y > 0 else m + y


def mod_solve(a, b, m):
    """
    Solve the equation ax = b mod m
    :param a:
    :param b:
    :param m:
    :return: An array with all x solving the equation
    """
    g = gcd(a, m)
    if b % g != 0:
        raise ValueError("The equation is not solvable")
    inverse = mod_inverse(a // g, m // g)
    x = inverse * (b // g) % 13
    return [x + k * (m // g) for k in range(g)]


def mod_power(a, exponent, m):
    """
    Compute a**exponent mod m
    :param a:
    :param exponent:
    :param m:
    :return:
    """
    if a > m:
        a = a % m
    if exponent == 0:
        return 1
    if exponent == 1:
        return a
    half = mod_power(a, exponent // 2, m)
    return half * half % m if is_even(exponent) else half * half * a % m


def remove_powers_of_2(n: int):
    number = n
    powers = 0
    while is_even(number):
        powers += 1
        number //= 2
    return powers, number


def is_probably_prime(n: int, iterations: int = 10) -> bool:
    """
    Miller-Rabin primality test
    :param n: the integer to check for primality
    :param iterations: maximum number of attempts
    :return: true or false
    """
    assert n > 1, "The argument must be an integer greater than 1"
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    k, s = remove_powers_of_2(n - 1)
    for _ in range(iterations):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(k - 1):
            x = mod_power(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def random_number(number_of_digits: int):
    range_start = 10 ** (number_of_digits - 1)
    range_end = (10 ** number_of_digits) - 1
    return random.randint(range_start, range_end)


def generate_random_prime(number_of_digits: int) -> int:
    """
    Generate a random prime number with a given number of digits
    :param number_of_digits: number of digits
    :return: a number that passes the Miller-Rabin primality test, and therefore is probably a prime
    """
    attempts: int = 0
    n = random_number(number_of_digits)

    while True:
        attempts += 1
        if is_even(n):
            n = n + 1
            continue
        if is_probably_prime(n):
            logging.info(f'Found a prime in {attempts} attempts')
            return n
        n = n + 1
