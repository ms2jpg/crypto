import sys

with open(sys.argv[1], 'rb') as f:
    a = f.read()

with open(sys.argv[2], 'rb') as f:
    b = f.read()

def convert_to_bits(array):
    return list(''.join(list(map(lambda x: bin(x)[2:], list(array)))))

def diff(a1, a2):
    return ['x' if e1 != e2 else e1 for e1, e2 in zip(a1, a2)]

a_bits = convert_to_bits(a)
b_bits = convert_to_bits(b)
print(''.join(a_bits))
print(''.join(b_bits))
diff_bits = ''.join(diff(a_bits, b_bits))
ratio = diff_bits.count('x') / len(diff_bits)
print(diff_bits)
print(ratio)
