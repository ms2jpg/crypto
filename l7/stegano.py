import imageio as iio

# read an image

class Stegano:
    def __init__(self, path):
        self.img = iio.imread(path)
        self.max_message_size = int(len(self.img) * len(self.img[0]) * 3 / 8) - 3

    def position(self):
        for a in range(len(self.img)):
            for b in range(len(self.img[a])):
                for c in range(len(self.img[a][b])):
                    yield [a, b, c]
        return False

    @staticmethod
    def to_bits(s):
        result = []
        for c in s:
            bits = bin(c)[2:]

            bits = '00000000'[len(bits):] + bits
            result.extend([int(b) for b in bits])
        return result

    @staticmethod
    def from_bits(bits):
        chars = []
        for b in range(len(bits) / 8):
            byte = bits[b * 8:(b + 1) * 8]
            chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        return ''.join(chars)

    def embed_message(self, msg):
        if len(msg) > self.max_message_size:
            raise Exception('Max message size exceeded')
        msg_bits = Stegano.to_bits(msg + b'\n\n\n')
        pos_gen = self.position()
        for bit in msg_bits:
            row, col, cpos = next(pos_gen)
            if bit:
                self.img[row][col][cpos] = self.img[row][col][cpos] | 1
            else:
                self.img[row][col][cpos] = self.img[row][col][cpos] & 0xfe

    def get_message(self):
        message = bytearray([])
        buf = []
        for row, col, cpos in self.position():
            if len(message) >= 3 and message[-3:] == b'\n\n\n':
                break
            if len(buf) >= 8:
                number = 0
                for bit in buf:
                    number = (number << 1) | bit
                message.append(number)
                buf = []
            byte = self.img[row][col][cpos]
            buf.append(byte % 2)
        return message[:-3]

    def save_image(self, path):
        iio.imwrite(path, self.img)


# s = Stegano('image.bmp')
# s.embed_message("politechnika")
# s.save_image('hidden.bmp')

#
# s = Stegano('hidden.bmp')
# print(s.get_message())