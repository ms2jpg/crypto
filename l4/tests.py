import glob
import math

def ones(data):
    number_of_ones = sum(map(int, data))
    return 9275 < number_of_ones < 10275, number_of_ones


def series(data):
    ranges = {
        1: [2315, 2685],
        2: [1114, 1386],
        3: [527, 723],
        4: [240, 384],
        5: [103, 209],
        6: [103, 209],
    }

    s = [{}, {}]
    for i in range(1, 6 + 1):
        s[0][i] = 0
        s[1][i] = 0
    last_bit = data[0]
    count = 0
    for bit in data:
        if bit == last_bit:
            count += 1
        else:
            if count > 6:
                count = 6
            s[int(last_bit)][count] += 1
            last_bit = bit
            count = 1
    if count > 6:
        count = 6
    s[int(last_bit)][count] += 1
    for e in s:
        for key in e:
            if not (ranges[key][0] < e[key] < ranges[key][1]):
                return False, s
    return True, s


def long_series(data):
    last_bit = data[0]
    max_count = 0
    count = 0
    for bit in data:
        if bit == last_bit:
            count += 1
        else:
            if max_count < count:
                max_count = count
            if count >= 26:
                return False
            last_bit = bit
            count = 1
    if count >= 26:
        return False, max_count
    return True, max_count

def poker(data):
    chunk_size = 4
    quantities = [0 for _ in range(2 ** chunk_size)]
    for chunk_offset in range(math.floor(len(data) / chunk_size)):
        chunk = data[chunk_size * chunk_offset:chunk_size * (chunk_offset + 1)]
        quantities[int(chunk, 2)] += 1
    x = 16 / 5000 * sum(map(lambda s: s ** 2, quantities)) - 5000
    return 2.16 < x < 46.17, {'quantities': quantities, 'x': x}

tests = {
    'single bit': ones,
    'series': series,
    'long_series': long_series,
    'poker': poker
}

for filename in glob.glob('20k-*.txt'):
    print(f'Testfile {filename}:')
    with open(filename) as f:
        data = f.read().strip()
    if len(data) < 20000:
        print(f'{filename} is shorter than 20KB')
        continue
    if len(data) > 20000:
        data = data[0:20000]

    for test_name in tests:
        test_result, test_data = tests[test_name](data)
        print(' ' * 2, '[OK]' if test_result else '[FAIL]', f'{test_name} test', test_data)
    print('')

