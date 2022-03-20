import os
import glob
import secrets
import random

input_folder = 'encrypted'
output_folder = 'corrupted'

class Corrupt:
    @staticmethod
    def split_block(data, size):
        output_data = []
        for i in range(0, len(data), size):
            output_data.append(data[i:i + size])
        return output_data

    @staticmethod
    def delete_block(data):
        data.pop(2)
        return data

    @staticmethod
    def duplicate_block(data):
        data.insert(2, data[2])
        return data

    @staticmethod
    def block_swap(data):
        data[2], data[3] = data[3], data[2]
        return data

    @staticmethod
    def add_random_block(data):
        block = secrets.token_bytes(16)
        data.insert(2, block)
        return data

    @staticmethod
    def modify_one_byte(data):
        byte_no = random.randint(16, len(data)*16-16)
        block_no = int(byte_no / 16)
        byte_no = byte_no % 16
        block = list(data[block_no])
        block[byte_no] = random.randint(0, 255)
        data[block_no] = bytearray(block)
        return data

    @staticmethod
    def swap_bytes_in_block(data):
        block = list(data[3])
        block[6], block[7] = block[7], block[6]
        data[3] = bytes(block)
        return data

    @staticmethod
    def delete_byte(data):
        xd = list(data[3])
        xd.pop(6)
        data[3] = bytes(xd)
        return data


corrupt_methods = {
    'delete_block': Corrupt.delete_block,
    'duplicate_block': Corrupt.duplicate_block,
    'block_swap': Corrupt.block_swap,
    'add_random_block': Corrupt.add_random_block,
    'modify_one_byte': Corrupt.modify_one_byte,
    'swap_bytes_in_block': Corrupt.swap_bytes_in_block,
    'delete_byte': Corrupt.delete_byte,

}

for input_file_path in glob.glob(f'{input_folder}/*'):
    with open(input_file_path, 'rb') as input_file:
        data = Corrupt.split_block(input_file.read(), 16)
    for cm_name in corrupt_methods:
        corrupted_blocks = corrupt_methods[cm_name](data[:])
        corrupted_data = b''
        for block in corrupted_blocks:
            corrupted_data += block
        name = input_file_path.split('/')[-1].split('.')[0]
        with open(f'corrupted/{name}_{cm_name}.bin', 'wb') as output_file:
            output_file.write(corrupted_data)
        print(f'corrupted/{name}_{cm_name}.bin')


