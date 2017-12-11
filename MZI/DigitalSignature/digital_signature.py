from hashlib import md5

import sys
from rsa import newkeys
from rsa.common import byte_size
from rsa.core import decrypt_int, encrypt_int


def sign_bytes(message, private_key):
    hash_int = int.from_bytes(md5(message).digest(), sys.byteorder)
    signature_int = encrypt_int(hash_int, private_key.d, private_key.n)

    key_length = byte_size(private_key.n)
    return signature_int.to_bytes(key_length, sys.byteorder)


def verify_sign(message, public_key, signature):
    signature_int = int.from_bytes(signature, sys.byteorder)
    decrypted_hash = decrypt_int(signature_int, public_key.e, public_key.n)

    hash_int = int.from_bytes(md5(message).digest(), sys.byteorder)
    return hash_int == decrypted_hash


if __name__ == '__main__':
    public, private = newkeys(256)
    print(public, '\n', private)

    message = b'qwerty ytrewq'
    signature = sign_bytes(message, private)
    print(message, '\n', signature)
    print(verify_sign(message, public, signature))
