import string

CAPS = list(string.ascii_uppercase)
CAP_INDEX = {letter: number for (letter, number) in zip(CAPS, range(1, len(CAPS) + 1))}


def encode_caps(text: string) -> int:
    return int(''.join(['{:02d}'.format(CAP_INDEX[c]) for c in text]))


def decode_caps(number: int) -> string:
    codeword = str(number)
    if len(codeword) % 2 != 0:
        codeword = '0' + codeword
    return ''.join([CAPS[int(codeword[i:i + 2]) - 1] for i in range(0, len(codeword) - 1, 2)])


def encode_ascii(text: string) -> int:
    return int(''.join(['{:03d}'.format(ord(character)) for character in text]))


def decode_ascii(number: int) -> string:
    codeword = str(number)
    # account for the possibility that there are one or two zeros in the front
    while len(codeword) % 3 != 0:
        codeword = '0' + codeword
    return ''.join([chr(int(codeword[i:i + 3])) for i in range(0, len(codeword) - 2, 3)])

