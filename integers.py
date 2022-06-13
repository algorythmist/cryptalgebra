def is_even(n):
    return n % 2 == 0


def gcd(n1: int, n2: int) -> int:
    assert (n1 >= 0 and n2 >= 0), "Arguments must be non-negative integers"
    if n1 < n2:
        return gcd(n2, n1)
    return n1 if n2 == 0 else gcd(n2, n1 % n2)


def lcm(n1: int, n2: int) -> int:
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
    :param a:
    :param m:
    :return:
    """
    assert m > 0 and a >= 0, "Arguments must be positive integers"
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
    return half*half % m if is_even(exponent) else half*half*a % m

