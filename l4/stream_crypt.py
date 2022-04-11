from bbs import *
import argparse
import numpy as np

if __name__ == "__main__":


    parser = argparse.ArgumentParser(description='Encrypt or decrypt message using AES')

    parser.add_argument('-i', '--input-file', help='Input file', required=True)
    parser.add_argument('-o', '--output-file', help='Output file', required=True)
    parser.add_argument('-s', '--seed-file', help='Seed file')

    args = parser.parse_args()
    filename = args.input_file
    with open(filename, 'rb') as f:
        data = f.read()
    length = len(data)
    if args.seed_file:
        with open(args.seed_file) as f:
            sc = json.load(f)
            generator = BBS(sc['p'], sc['q'], sc['seed'])
    else:
        p, q = generate_two_congurent_primes_in_range(1000000, 2000000)
        generator = BBS(p, q)
    bits = [int(''.join(x), 2) for x in np.array_split(list(generator.generate_bits(length * 8)), length)]


    ciphertext = bytes([_a ^ _b for _a, _b in zip(data, bits)])
    with open(args.output_file, 'wb') as f:
        f.write(ciphertext)



    # a = BBS(p, q)
    # l = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    # x = a.generate_bits(l)
    # print(x, end='')