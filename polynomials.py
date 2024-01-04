class Polynomial:
    def __init__(self, *coefficients: int):
        # discard leading zero coefficients from the right
        while coefficients and coefficients[-1] == 0:
            coefficients = coefficients[:-1]
        self.coefficients = coefficients

    def __repr__(self):
        def _terms():
            for i, a in enumerate(self.coefficients):
                if a:
                    yield f'{a}' if i == 0 \
                        else 'x' if i == 1 and a == 1 \
                        else f'{a}x' if i == 1 \
                        else f'x^{i}' if a == 1 else f'{a}x^{i}'

        return ' + '.join(_terms())

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        order = max(self.order(), other.order())
        return Polynomial(*(self._get(i) + other._get(i) for i in range(order + 1)))

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __isub__(self, other):
        return self - other

    def __neg__(self):
        return Polynomial(*(-a for a in self.coefficients))

    def __mul__(self, other):
        result_order = self.order() + other.order()
        coeff = [0] * (result_order + 1)
        for k in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                coeff[k + j] += self.coefficients[k] * other.coefficients[j]
        return Polynomial(*coeff)

    def __imul__(self, other):
        return self * other

    def __call__(self, x):
        return self.evaluate(x)

    def evaluate(self, x):
        return sum(a * x ** i for i, a in enumerate(self.coefficients))

    def order(self):
        return len(self.coefficients) - 1

    @property
    def degree(self):
        return self.order()

    def __eq__(self, other):
        return self.coefficients == other.coefficients

    def _get(self, index):
        return 0 if index >= len(self.coefficients) else self.coefficients[index]

    def __getitem__(self, index):
        return self.coefficients[index] if index < len(self.coefficients) else 0

    def is_monomial(self) -> bool:
        return all(coeff == 0 for coeff in self.coefficients[:-1])

    def __pow__(self, exponent: int):
        if exponent == 0:
            return Polynomial.zero()  # Return zero polynomial

        if exponent == 1:
            return self  # Return the polynomial itself

        if self.is_monomial():
            deg = self.degree * exponent
            return Polynomial.monomial(deg, self.coefficients[self.degree])

        half = self**(exponent // 2)
        squared = half * half

        if exponent % 2 == 0:  # If exponent is even
            return squared
        else:
            return squared * self

    @staticmethod
    def monomial(degree, coefficient):
        return Polynomial(*([0] * degree + [coefficient]))

    @staticmethod
    def is_zero(poly):
        return poly.order() == 0 and poly.coefficients[0] == 0

    @staticmethod
    def zero():
        return Polynomial(0)
