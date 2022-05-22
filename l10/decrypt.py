import sys
import math
message_file = sys.argv[1]
destination_file = sys.argv[2]


class RSAEncrypt:
    def __init__(self, privkey_file, message_file, destination_file):
        # open private key
        with open(privkey_file) as f:
            self.n, self.d = map(int, f.read().split('\n'))

        # open message
        with open(message_file, 'rb') as f:
            self.ciphertext = f.read()
        chunk_size = RSAEncrypt.calculate_chunk_size(self.n)
        n_size = math.ceil(RSAEncrypt.get_int_size(self.n) / 8)

        message = b''

        for chunk in RSAEncrypt.chunks(self.ciphertext, n_size):
            m = self.decrypt(int.from_bytes(chunk, byteorder=sys.byteorder), self.d, self.n)
            message += m.to_bytes(chunk_size, byteorder=sys.byteorder)
        # unpad
        while len(message) and message[-1] == b'\0':
            message.pop()

        with open(destination_file, 'wb') as f:
            f.write(message)



    def decrypt(self, m, a, n):
        w = 1
        bits = []
        e = a
        while a:
            bits.append(a & 1)
            a >>= 1
        bits = bits[::-1]

        for bit in bits:
            w = w ** 2 % n
            if bit == 1:
                w = w * m % n
        return w

    @staticmethod
    def get_int_size(_n):
        b = 0
        while _n:
            b += 1
            _n >>=1
        return b

    @staticmethod
    def calculate_chunk_size(number):
        b = RSAEncrypt.get_int_size(number)
        return b // 8

    @staticmethod
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

encryptor = RSAEncrypt('id_rsa', 'encrypted.txt', 'payload.txt')

# for char in payload:
#     print(encrypt(char, e, n))
# encrypted = encrypt(payload, e, n)
# with open(destination_file, 'w') as f:
#     f.write(str(encrypted))
