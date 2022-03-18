from aes_ecb import *
import utils


class AES_CBC(AES_ECB):
    def __init__(self, key, iv=None, verbose=False):
        super().__init__(key)
        if iv is None:
            # iv = os.urandom(AES_ECB.BLOCK_SIZE)
            iv = utils.get_random_unicode(AES_ECB.BLOCK_SIZE).encode('utf-8')
        elif type(iv) == str:
            iv = iv.encode('utf-8')
        self.iv = iv
        self.verbose = verbose

    def encrypt(self, msg):
        msg = AES_ECB.pad(msg)
        encrypted = b''
        v = self.iv
        for block in AES_ECB.split_block(msg, AES_ECB.BLOCK_SIZE):
            new_block = AES_ECB.byte_xor(block, v)
            new_block = self.aes.encrypt(new_block)
            encrypted += new_block
            if self.verbose:
                print(block, '->', new_block.hex())
            v = new_block
        return encrypted

    def decrypt(self, msg):
        v = self.iv
        decrypted = b''
        for block in AES_ECB.split_block(msg, AES_ECB.BLOCK_SIZE):
            new_block = self.aes.decrypt(block)
            new_block = AES_ECB.byte_xor(new_block, v)
            new_block = AES_ECB.unpad(new_block)
            if self.verbose:
                print(block.hex(), '->', new_block)
            v = block
            decrypted += new_block
            # print(new_block)
        return decrypted
