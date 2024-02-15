"""
Attacks on Elliptic Curve Cryptography
"""
from random import randint
from typing import Dict

from elliptic import EllipticCurve, Point
from integers import is_probably_prime, mod_inverse


def naive_prime_attack(ec: EllipticCurve, p: Point, order: int, q: Point,
                       iterations: int = 1000) -> int:
    assert is_probably_prime(order), "The order must be a prime number"

    def find_dupes() -> tuple[int, int, int, int] | None:
        lookup: Dict[Point, tuple[int, int]] = {}
        for _ in range(iterations):
            c = randint(1, 228)
            d = randint(1, 228)
            result = ec.add(ec.multiply(p, c), ec.multiply(q, d))
            if result in lookup:
                e, f = lookup[result]
                if e != c or f != d:
                    return c, d, e, f
            lookup[result] = (c, d)
        return None

    result = find_dupes()
    if not result:
        raise ValueError("No solution found")
    c, d, e, f = result
    return (c - e) * mod_inverse(f - d, order) % order
