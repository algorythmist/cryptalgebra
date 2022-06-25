from encoders import *


def test_encode_caps():
    encoded = encode_caps(CAPS)
    assert 102030405060708091011121314151617181920212223242526 == encoded
    decoded = decode_caps(encoded)
    assert ''.join(CAPS) == decoded

    encoded = encode_caps('HAMSTER')
    assert 8011319200518 == encoded
    decoded = decode_caps(encoded)
    assert 'HAMSTER' == decoded


def test_encode_ascii():
    encoded = encode_ascii('Zebra')
    assert 90101098114097 == encoded
    assert 'Zebra' == decode_ascii(90101098114097)

