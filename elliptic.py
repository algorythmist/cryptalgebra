from integers import mod_inverse


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
        return f"y^2 = x^3 + {self.a}x + {self.b}, mod {self.p})"

    def __str__(self):
        return self.__repr__()

    def is_valid_point(self, x, y):
        """
        Check if the point (x, y) is a valid point on the curve.
        """
        return (y * y - x * x * x - self.a * x - self.b) % self.p == 0

    def determinant(self):
        """
        Return the determinant of the curve.
        """
        return -16 * (4 * self.a * self.a * self.a + 27 * self.b * self.b) % self.p

    def add(self, p1, p2):
        """
        Add two points p1 = (x1, y1) and p2 = (x2, y2) on the curve.
        """
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2 and y1 == y2:
            return self.double(x1, y1)
        if x1 == x2 and y1 != y2:
            return None
        slope = (y1 - y2) * mod_inverse(x1 - x2, self.p) % self.p
        x3 = (slope * slope - x1 - x2) % self.p
        y3 = (slope * (x1 - x3) - y1) % self.p
        return x3, y3

    def double(self, point):
        """
        Double the point (x, y) on the curve.
        """
        x, y = point
        slope = (3 * x * x + self.a) * mod_inverse(2 * y, self.p) % self.p
        xr = (slope * slope - 2 * x) % self.p
        yr = (slope * (x - xr) - y) % self.p
        return xr, yr

    def negate(self, point):
        """
        Negate the point (x, y) on the curve.
        """
        x, y = point
        return x, -y % self.p