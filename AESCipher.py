from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


pad = lambda s: s + (16 - len(s) % 16) * " "
unpad = lambda s: (s.decode("utf-8")).strip(' ')
hasher = lambda x: SHA256.new(bytes(x, "utf-8")).digest()


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
