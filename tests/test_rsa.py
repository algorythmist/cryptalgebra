from rsa import *


def test_rsa_encode():
    p = 885320963
    q = 238855417
    e = 9007
    m = 30120
    encrypted = rsa_encode(p, q, e, m)
    assert 113535859035722866 == encrypted
    decrypted = rsa_decode(p, q, e, encrypted)
    assert m == decrypted



