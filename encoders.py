"""
Tools to convert from text to integers and vice versa
"""

import string

CAPS = list(string.ascii_uppercase)
CAP_INDEX = {letter: number for (letter, number) in zip(CAPS, range(1, len(CAPS) + 1))}


def encode_caps(text: string) -> int:
    """
    Convert a string consisting only of capital letters to a number using the mapping
    A -> 01, B -> 02, et cetera.
    :param text: the all-capps text
    :return: an integer
    """
    return int(''.join(['{:02d}'.format(CAP_INDEX[c]) for c in text]))


def decode_caps(number: int) -> string:
    """
    Inverse of encode_caps
    :param number: A number corresponding to an all-caps string
    :return: the original string
    """
    codeword = str(number)
    if len(codeword) % 2 != 0:
        codeword = '0' + codeword
    return ''.join([CAPS[int(codeword[i:i + 2]) - 1] for i in range(0, len(codeword) - 1, 2)])


def encode_ascii(text: string) -> int:
    """
    Convert a string to an integer consisting of the ascii value of each character
    :param text: any ascii string
    :return: the integer encoding the text
    """
    return int(''.join(['{:03d}'.format(ord(character)) for character in text]))


def decode_ascii(number: int) -> string:
    """
    Compute the inverse of encode_ascii
    :param number: the encoded string
    :return: the original string
    """
    codeword = str(number)
    # account for the possibility that there are one or two zeros in the front
    while len(codeword) % 3 != 0:
        codeword = '0' + codeword
    return ''.join([chr(int(codeword[i:i + 3])) for i in range(0, len(codeword) - 2, 3)])

