import socket
import hashlib
import sys

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)


def main():
    host = sys.argv[1]
    port = 4000
    server = (host, port)
    # Hardcoded key and initialization vector
    iv = b'secureivl337'
    key = b'thisisaverysecretkeyl337'

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    checksum = sending_receiving(s, server)

    while True:
        s.sendto(b"final", server)
        cipher_text = bytes(recv(s))
        s.sendto(b"final", server)
        tag = bytes(recv(s))
        decrypted_text = decrypt(key, iv, cipher_text, tag)
        if hashlib.sha256(decrypted_text).hexdigest() != checksum:
            continue
        else:
            print(f"flag: {decrypted_text}")
            break

def sending_receiving(s, server):
    s.sendto(b"hello", server)
    print(recv(s))
    s.sendto(b"ready", server)
    data = recv(s)
    print(data)
    checksum = data[104:136].hex()
    return checksum

def recv(s):
    try:
        data = s.recv(1024)
        return data
    except Exception as e:
        print(str(e))

def decrypt(key, iv, cText, tag):
    #Create AES GCM decryptor object
    decryptor = Cipher(algorithms.AES(key), modes.GCM(iv, tag),
    backend = default_backend()).decryptor()

    return decryptor.update(cText) + decryptor.finalize()

if __name__ == '__main__':
    main()