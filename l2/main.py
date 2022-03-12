import argparse
from aes_ecb import AES_ECB
from aes_cbc import AES_CBC
import utils

parser = argparse.ArgumentParser(description='Encrypt or decrypt message using AES')

parser.add_argument('-e', '--encrypt', help='Encrypt message', action='store_true')
parser.add_argument('-d', '--decrypt', help='Decrypt message', action='store_true')
parser.add_argument('-m', '--mode', choices=['aes-ecb', 'aes-cbc'], required=True, help='AES block mode')
parser.add_argument('-i', '--input', required=True, help='Input file')
parser.add_argument('-o', '--output', required=True, help='Output file')
parser.add_argument('-p', '--password', required=False, help='Password')
parser.add_argument('-iv', '--initial-value', required=False, help='Initial value (only acceptable for AES-CBC)')
parser.add_argument('-ivt', '--initial-value-type', choices=['raw', 'hex'], required=False, help='Initial value type')
parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')
args = parser.parse_args()
message = ''
try:
    with open(args.input, 'rb') as input_file:
        message = input_file.read()
except FileNotFoundError:
    print(f'[ERROR] No such input file: {args.input}')
    exit()
except UnicodeDecodeError:
    print('[ERROR] Input file can\'t be converted to UTF-8!')
    exit()

if args.password is None:
    args.password = input('Password: ')

if len(args.password) not in [16, 24, 32]:
    print('[ERROR] AES key must be either 16, 24, or 32 bytes long')
    exit()

key = ''
try:
    key = args.password.encode('utf-8')
except UnicodeDecodeError:
    print('[ERROR] Password must be in UTF-8')

if args.mode == 'aes-ecb':
    crypt = AES_ECB(key, verbose=args.verbose)
elif args.mode == 'aes-cbc':
    if args.initial_value_type == 'hex':
        args.initial_value = bytearray.fromhex(args.initial_value)
    crypt = AES_CBC(key, iv=args.initial_value, verbose=args.verbose)
    if args.initial_value is None:
        if args.initial_value_type is None or args.initial_value_type == 'hex':
            print(f'Initial value: {crypt.iv.hex()}')
        else:
            print(f'Initial value: {crypt.iv}')
output = ''
if args.encrypt:
    output = crypt.encrypt(message)
elif args.decrypt:
    output = crypt.decrypt(message)


with open(args.output, 'wb') as output_file:
    output_file.write(output)
