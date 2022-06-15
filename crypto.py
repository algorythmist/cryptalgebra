import random

from integers import mod_inverse, mod_power, generate_random_prime


class RSA:

    def __init__(self, p=None, q=None, e=None):
        self.p = p if p else generate_random_prime(101)
        self.q = q if q else generate_random_prime(99)
        self.e = e if e else generate_random_prime(10)
        self.n = self.p * self.q
        self.d = mod_inverse(self.e, (self.p - 1) * (self.q - 1))

    def get_public_key(self):
        return self.e, self.n

    def encrypt_int(self, message: int) -> int:
        return mod_power(message, self.e, self.n)

    def decrypt_int(self, encrypted_message: int) -> int:
        return mod_power(encrypted_message, self.d, self.n)


class ElGamal:

    def __init__(self, p=None, generator=None, secret=None):
        """
        El Gamal crypto system
        :param p: A prime
        :param generator: a primitive root of p
        :param secret: the secret exponent
        """
        self.p = p if p else generate_random_prime(101)
        self.generator = generator if generator else generate_random_prime(10)
        self.secret = secret if secret else random.randint(2, p - 1)
        self.public_key = mod_power(self.generator, self.secret, p)

    def get_public_key(self):
        return self.p, self.generator, self.public_key

    def encrypt_int(self, message: int) -> int:
        power = random.randint(2, self.p - 1)
        r = mod_power(self.generator, power, self.p)
        t = (mod_power(self.public_key, power, self.p) * message) % self.p
        return r, t

    def decrypt_pair(self, r: int, t: int):
        return (mod_power(r, self.p - self.secret - 1, self.p) * t) % self.p
