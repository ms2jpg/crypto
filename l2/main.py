from Crypto.Cipher import AES
import os
import random


def get_random_unicode(length):
    try:
        get_char = unichr
    except NameError:
        get_char = chr

    # Update this to include code point ranges to be sampled
    include_ranges = [
        ( 0x0021, 0x0021 ),
        ( 0x0023, 0x0026 ),
        ( 0x0028, 0x007E ),
        ( 0x00A1, 0x00AC ),
        ( 0x00AE, 0x00FF ),
        ( 0x0100, 0x017F ),
        ( 0x0180, 0x024F ),
        ( 0x2C60, 0x2C7F ),
        ( 0x16A0, 0x16F0 ),
        ( 0x0370, 0x0377 ),
        ( 0x037A, 0x037E ),
        ( 0x0384, 0x038A ),
        ( 0x038C, 0x038C ),
    ]

    alphabet = [
        get_char(code_point) for current_range in include_ranges
            for code_point in range(current_range[0], current_range[1] + 1)
    ]
    return ''.join(random.choice(alphabet) for i in range(length))




class AES_ECB:
    BLOCK_SIZE = 16  # Bytes

    def __init__(self, key):
        self.key = key
        self.aes = AES.new(self.key, AES.MODE_ECB)

    def encrypt(self, raw):
        raw = self.pad(raw)
        return self.aes.encrypt(raw)

    def decrypt(self, enc):
        return self.unpad(self.aes.decrypt(enc))

    @staticmethod
    def pad(s):
        return s + ((AES_ECB.BLOCK_SIZE - len(s) % AES_ECB.BLOCK_SIZE) * chr(
            AES_ECB.BLOCK_SIZE - len(s) % AES_ECB.BLOCK_SIZE)).encode('utf-8')

    @staticmethod
    def unpad(s):
        last_byte = s[-1]
        if last_byte > AES_ECB.BLOCK_SIZE:
            return s
        if all(b == last_byte for b in s[AES_ECB.BLOCK_SIZE - last_byte:]):
            return s[:AES_ECB.BLOCK_SIZE - last_byte]
        return s

    @staticmethod
    def sxor(s1, s2):
        return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

    @staticmethod
    def byte_xor(ba1, ba2):
        return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

    @staticmethod
    def split_block(data, size):
        for i in range(0, len(data), size):
            yield data[i:i + size]


class AES_CBC(AES_ECB):
    def __init__(self, key, iv=None):
        super().__init__(key)
        if iv is None:
            # iv = os.urandom(AES_ECB.BLOCK_SIZE)
            iv = get_random_unicode(AES_ECB.BLOCK_SIZE).encode('utf-8')
        self.iv = iv
        print('iv:', self.iv.decode('utf-8'))

    def encrypt(self, msg):
        print('encryption')
        msg = AES_ECB.pad(msg)
        encrypted = b''
        v = self.iv
        for block in AES_ECB.split_block(msg, AES_ECB.BLOCK_SIZE):
            new_block = AES_ECB.byte_xor(block, v)
            new_block = self.aes.encrypt(new_block)
            encrypted += new_block
            print(block, '->', new_block.hex())
            v = new_block
        return encrypted

    def decrypt(self, msg):
        print('decryption')
        v = self.iv
        for block in AES_ECB.split_block(msg, AES_ECB.BLOCK_SIZE):
            new_block = self.aes.decrypt(block)
            new_block = AES_ECB.byte_xor(new_block, v)
            new_block = AES_ECB.unpad(new_block)
            print(block.hex(), '->', new_block)
            v = block
            # print(new_block)


message = '''co cie boli? czy az tak cie to boli? ze rysiu peja ma dzis szanse ucziciwie zarobic?'''
x = AES_CBC(('a' * 16).encode('utf-8'), b'b'*16)

x.decrypt(x.encrypt(message.encode('utf-8')))
