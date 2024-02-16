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

class PohlighHellman:

    def __init__(self, ec: EllipticCurve, p: Point, order: int, q: Point):
        self.ec = ec
        self.p = p
        self.order = order
        self.q = q

    def _expand(self, z: list[int], prime: int) -> Point:
        result = None
        for i, c in enumerate(z):
            component = self.ec.multiply(self.p, c*prime**i)
            result = component if result is None else self.ec.add(result, component)
        return result

    def _determine_prime_representation(self, prime: int, power: int):
        p0 = self.ec.multiply(self.p, self.order // prime)
        z: list[int] = []
        for i in range(power):
            if len(z) == 0:
                q0 = self.ec.multiply(self.q, self.order // prime)
            else:
                expansion = self._expand(z, prime)
                q0 = self.ec.multiply(self._expand(z, prime), self.order // (prime**(i+1)))
            z[i] = naive_prime_attack(self.ec, self.p, prime, self.q)




