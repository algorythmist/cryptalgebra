from integers import gcd


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
    return [a for a in range(2, p) if len(compute_cycle(a, p)) == p-1]
