from crypto import *


def test_rsa_encrypt_decrypt():
    p = 885320963
    q = 238855417
    e = 9007
    rsa = RSA(p=p,q=q,e=e)
    message = 30120
    encrypted = rsa.encrypt_int(message)
    assert 113535859035722866 == encrypted
    decrypted = rsa.decrypt_int(encrypted)
    assert message == decrypted


def test_rsa_generated():
    rsa = RSA()
    message = 30120
    encrypted = rsa.encrypt_int(message)
    decrypted = rsa.decrypt_int(encrypted)
    assert message == decrypted
