from aes_ecb import *
import utils
import sys

class AES_CTR(AES_ECB):
    def __init__(self, key, iv=None, verbose=False):
        super().__init__(key)
        if iv is None:
            self.iv = utils.get_random_unicode(AES_ECB.BLOCK_SIZE).encode('utf-8')[:AES_ECB.BLOCK_SIZE]
        elif type(iv) == str:
            self.iv = iv.encode('utf-8')
        else:
            self.iv = iv
        self.verbose = verbose

    def ctr(self, block_number):
        ctr = list(self.iv)
        ctr[-1] += block_number
        for i in range(len(ctr)):
            if ctr[-i] > 255:
                overflow = int(ctr[-i] / 256)
                ctr[-i] %= 256
                if i+1 >= len(ctr):
                    break
                else:
                    ctr[-(i+1)] += overflow
            else:
                break
        # iv = int.from_bytes(self.iv, byteorder=sys.byteorder)
        # ctr = (iv + block_number).to_bytes(16, sys.byteorder)
        return self.aes.encrypt(bytes(ctr))

    def encrypt(self, msg):
        msg = AES_ECB.pad(msg)
        encrypted = b''
        i = 0
        for block in AES_ECB.split_block(msg, AES_ECB.BLOCK_SIZE):
            ctr = self.ctr(i)
            # print(i, ctr)
            new_block = AES_ECB.byte_xor(block, ctr)
            if self.verbose:
                print(block, '->', new_block.hex())
            encrypted += new_block
            i += 1
        return encrypted

    def decrypt(self, msg):
        decrypted = b''
        i = 0
        for block in AES_ECB.split_block(msg, AES_ECB.BLOCK_SIZE):
            ctr = self.ctr(i)
            # print(i, ctr)
            print(block)
            new_block = AES_ECB.byte_xor(block, ctr)
            decrypted += self.unpad(new_block)
            if self.verbose:
                print(block.hex(), '->', new_block)
            # print(new_block)
            i +=  1
        return decrypted
