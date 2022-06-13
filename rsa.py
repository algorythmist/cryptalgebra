from integers import mod_inverse, mod_power


def rsa_encode(p: int, q: int, e: int, message: int) -> int:
    n = p * q
    return mod_power(message, e, n)


def rsa_decode(p: int, q: int, e: int, encrypted_message: int):
    n = (p-1)*(q-1)
    d = mod_inverse(e, n)
    return mod_power(encrypted_message, d, p*q)



