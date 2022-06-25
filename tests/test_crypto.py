from crypto import *
from encoders import *


def test_rsa_encrypt_decrypt_int():
    p = 885320963
    q = 238855417
    e = 9007
    rsa = RSA(p=p, q=q, e=e)
    message = 30120
    encrypted = rsa.encrypt_int(message)
    assert 113535859035722866 == encrypted
    decrypted = rsa.decrypt_int(encrypted)
    assert message == decrypted


def test_rsa_encrypt_decrypt_text_caps():
    p = 920221992241681268443
    q = 218900912992975223
    e = 9007
    rsa = RSA(p=p, q=q, e=e)
    message = 'CAT'
    encrypted = rsa.encrypt_text(message, encoder=encode_caps)
    decrypted = rsa.decrypt_text(encrypted, decoder=decode_caps)
    assert message == decrypted


def test_rsa_encrypt_decrypt_text_ascii():
    p = 920221992241681268443
    q = 218900912992975223
    e = 9007
    rsa = RSA(p=p, q=q, e=e)
    message = 'Zebra'
    encrypted = rsa.encrypt_text(message)
    decrypted = rsa.decrypt_text(encrypted)
    assert message == decrypted


def test_rsa_generated():
    rsa = RSA()
    message = 30120
    encrypted = rsa.encrypt_int(message)
    decrypted = rsa.decrypt_int(encrypted)
    assert message == decrypted


def test_elgamal():
    prime = 8661340973
    generator = 644263599
    el_gamal = ElGamal(p=prime, generator=generator)
    message = 30120
    r, t = el_gamal.encrypt_int(message)
    decrypted = el_gamal.decrypt_pair(r, t)
    assert message == decrypted
