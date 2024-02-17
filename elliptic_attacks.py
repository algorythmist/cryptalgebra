"""
Attacks on Elliptic Curve Cryptography
"""
from random import randint
from typing import Dict

from elliptic import EllipticCurve, Point
from integers import is_probably_prime, mod_inverse, solve_chinese_remainder
from factors import naive_factorization_with_multiplicity


def naive_prime_attack(ec: EllipticCurve, p: Point, prime_order: int, q: Point,
                       iterations: int = 10000) -> int:
    assert is_probably_prime(prime_order), "The order must be a prime number"
    if p == q:
        return 1

    def find_dupes() -> tuple[int, int, int, int] | None:
        lookup: Dict[Point, tuple[int, int]] = {}
        for _ in range(iterations):
            c = randint(1, prime_order - 1)
            d = randint(1, prime_order - 1)
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
    a = (c-e) % prime_order
    b = (f-d) % prime_order
    return a * mod_inverse(b, prime_order) % prime_order


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

    def _determine_prime_representation(self, prime: int, power: int) -> int:
        p0 = self.ec.multiply(self.p, self.order // prime)
        z: list[int] = []
        for i in range(power):
            if len(z) == 0:
                q = self.ec.multiply(self.q, self.order // prime)
            else:
                expansion = self._expand(z, prime)
                q = self.ec.subtract(self.q, expansion)
                q = self.ec.multiply(q, self.order // (prime**(i+1)))
            z.append(naive_prime_attack(self.ec, p0, prime, q))
        result = 0
        for i in range(power):
            result += z[i] * prime**i
        return result

    def solve(self):
        factors = naive_factorization_with_multiplicity(self.order)
        partials_ls = [(self._determine_prime_representation(prime, power), prime**power)
                       for prime, power in factors]
        return solve_chinese_remainder(partials_ls)

