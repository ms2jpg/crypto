from Crypto.Cipher import AES

class AES_ECB:
    BLOCK_SIZE = 16  # Bytes

    def __init__(self, key, verbose=False):
        self.key = key
        self.aes = AES.new(self.key, AES.MODE_ECB)
        self.verbose = verbose

    def encrypt(self, raw):
        raw = self.pad(raw)
        encrypted = b''
        for block in AES_ECB.split_block(raw, AES_ECB.BLOCK_SIZE):
            new_block = self.aes.encrypt(block)
            if self.verbose:
                print(block, '->', new_block.hex())
            encrypted += new_block
        return encrypted

    def decrypt(self, enc):
        decrypted = b''
        for block in AES_ECB.split_block(enc, AES_ECB.BLOCK_SIZE):
            new_block = self.aes.decrypt(block)
            if self.verbose:
                print(block.hex(), '->', new_block)
            decrypted += AES_ECB.unpad(new_block)
        return decrypted

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
            d = data[i:i + size]
            yield data[i:i + size]