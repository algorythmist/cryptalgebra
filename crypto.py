from integers import mod_inverse, mod_power, generate_random_prime


class RSA:

    def __init__(self, p=None, q=None, e=None):
        self.p = p if p else generate_random_prime(101)
        self.q = q if q else generate_random_prime(99)
        self.e = e if e else generate_random_prime(10)
        self.n = self.p * self.q
        m = (self.p - 1) * (self.q - 1)
        self.d = mod_inverse(self.e, m)

    def encrypt_int(self, message: int) -> int:
        return mod_power(message, self.e, self.n)

    def decrypt_int(self, encrypted_message: int) -> int:
        return mod_power(encrypted_message, self.d, self.n)

