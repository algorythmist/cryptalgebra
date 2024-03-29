from typing import Tuple

from integers import mod_inverse

Point = Tuple[int, int] | None


class EllipticCurve:

    def __init__(self, a, b, p):
        """
        The elliptic curve is defined by the equation y^2 = x^3 + ax + b
        over the field of integers modulo p.
        """
        self.a = a
        self.b = b
        self.p = p

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.p == other.p

    def __repr__(self):
        return f"y^2 = x^3 + {self.a}x + {self.b} (mod {self.p})"

    def __str__(self):
        return self.__repr__()

    def is_valid_point(self, p: Point) -> bool:
        """
        Check if the point (x, y) is a valid point on the curve.
        """
        if not p:
            return True
        x, y = p
        return (y * y - x * x * x - self.a * x - self.b) % self.p == 0

    def determinant(self) -> int:
        """
        Return the determinant of the curve.
        """
        return -16 * (4 * self.a * self.a * self.a + 27 * self.b * self.b) % self.p

    def add(self, p1: Point, p2: Point) -> Point:
        """
        Add two points p1 = (x1, y1) and p2 = (x2, y2) on the curve.
        """
        if not p1:
            return p2
        if not p2:
            return p1
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            return self.double((x1, y1)) if y1 == y2 else None
        slope = (y1 - y2) * mod_inverse(x1 - x2, self.p) % self.p
        x3 = (slope * slope - x1 - x2) % self.p
        y3 = (slope * (x1 - x3) - y1) % self.p
        return x3, y3

    def double(self, point: Point) -> Point:
        """
        Double the point (x, y) on the curve.
        """
        if not point:
            return None
        x, y = point
        slope = (3 * x * x + self.a) * mod_inverse(2 * y, self.p) % self.p
        xr = (slope * slope - 2 * x) % self.p
        yr = (slope * (x - xr) - y) % self.p
        return xr, yr

    def negate(self, point: Point) -> Point:
        """
        Negate the point (x, y) on the curve.
        """
        if not point:
            return None
        x, y = point
        return x, -y % self.p

    def subtract(self, p1: Point, p2: Point) -> Point:
        """
        Subtract two points p1 = (x1, y1) and p2 = (x2, y2) on the curve.
        """
        return self.add(p1, self.negate(p2))

    def multiply(self, point: Point, n: int) -> Point:
        """
        Multiply the point (x, y) by the scalar n.
        """
        if n == 0:
            return None
        if n & 1:
            return self.add(point, self.multiply(point, n - 1))
        return self.multiply(self.double(point), n >> 1)
