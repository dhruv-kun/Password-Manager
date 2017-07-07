from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


def pad(s):
    return s + (16 - len(s) % 16) * ' '


def unpad(s):
    try:
        return s.decode('utf-8').strip(' ')
    except UnicodeDecodeError:
        raise Exception("Still bytes. Possibly not decrypted.")


def hasher(x):
    return SHA256.new(bytes(x, 'utf-8')).digest()


def encrypt(key, text):
    iv = Random.new().read(AES.block_size)
    key = hasher(key)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    text = pad(text)
    cipherText = cipher.encrypt(text)
    return (iv + cipherText)


def decrypt(key, cipherText):
    key = hasher(key)
    iv = cipherText[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    text = cipher.decrypt(cipherText[16:])
    text = unpad(text)
    return (text)
