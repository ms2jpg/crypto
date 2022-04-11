from math import gcd
from random import randint, shuffle
import sys
import numpy
import json

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def coprime(a, b):
    return gcd(a, b) == 1


def is_congruent_number(number):
    return number % 4 == 3

class BBS:
    p = 0
    q = 0
    n = 0
    seed = 0
    generatedValues = []

    def __init__(self, p, q, sd=None):
        if not (is_prime(q) and is_prime(p)) or p == q:
            raise Exception("P | Q not prime")

        self.p = p
        self.q = q
        self.n = p * q
        self.set_seed(sd)

    def set_blum_int(self, p, q):
        if not (is_prime(q) and is_prime(p)) or p == q:
            raise Exception("P | Q not prime")
        self.p = p
        self.q = q
        self.n = p * q

    def set_seed(self, sd = None):
        if sd is not None:
            self.seed = sd
            return
        while not coprime(self.n, self.seed):
            self.seed = randint(0, self.n - 1)
        d = {
            'p': self.p,
            'q': self.q,
            'seed': self.seed
        }
        print(json.dumps(d), file=sys.stderr)

    def generate_bits(self, amount):
        prev = self.seed ** 2 % self.n
        bits_array = [str(prev % 2)]
        for _ in range(1, amount):
            prev = prev ** 2 % self.n
            bits_array.append(str(prev % 2))
        return ''.join(bits_array)


def generate_two_congurent_primes_in_range(lower, upper):
    nums = [i for i in range(lower, upper + 1)]
    shuffle(nums)
    congurentPrimes = []
    while nums != [] and len(congurentPrimes) != 2:
        current = nums.pop()
        if is_prime(current) and is_congruent_number(current):
            congurentPrimes.append(current)
    return congurentPrimes if len(congurentPrimes) == 2 else [-1, -1]


if __name__ == "__main__":
    p, q = generate_two_congurent_primes_in_range(1000000, 2000000)
    a = BBS(p, q)
    l = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    x = a.generate_bits(l)
    print(x, end='')
