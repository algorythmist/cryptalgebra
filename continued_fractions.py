
def compute_continued_fraction(numerator, denominator):
    """
    Find the continued fraction expansion of a rational number
    :param numerator: the numerator of the rational number
    :param denominator: the denominator of the rational number
    :return: an array of integers representing the continued fraction expansion
    """
    if denominator == 0:
        raise ValueError("Denominator should not be 0")
    return __compute(int(numerator), int(denominator))


def __compute(a, b):
    if b == 0:
        return []
    if a == 0:
        return [0]
    return [a//b] + __compute(b, a % b)


def continued_fraction_from_real(real, precision):
    denominator = 10 ** precision
    return compute_continued_fraction(real * denominator, denominator)


def restore(expansion):
    """
    Derive a rational number from its continued fraction expansion
    :return: the rational number
    """
    return __restore(expansion, 0)


def __restore(expansion, n):
    if n == len(expansion) - 1:
        return expansion[n]
    return expansion[n] + 1.0 / __restore(expansion, n + 1)


def find_convergent(expansion):
    p0 = expansion[0]
    q0 = 1
    p1 = 1 + expansion[0] * expansion[1]
    q1 = expansion[1]
    for i in range(2, len(expansion)):
        p2 = expansion[i] * p1 + p0
        q2 = expansion[i] * q1 + q0
        p0 = p1
        q0 = q1
        p1 = p2
        q1 = q2
    return p1, q1