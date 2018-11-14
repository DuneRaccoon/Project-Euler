from math import sqrt
from q3 import *

def quad_formula(a,b,n):
    return n**2 + a*n + b

def is_prime(N):
    if N == 2:
        return True
    if N < 2 or N % 2 == 0:
        return False
    N_index = (N - 1) // 2
    primes_sieve = [True] * (N_index + 1)
    for n in range(1, (round(sqrt(N)) + 1) // 2):
        if primes_sieve[n]:
            if N % (2 * n + 1) == 0:
                return False
            for i in range(2 * n * (n + 1), N_index + 1, 2 * n + 1):
                primes_sieve[i] = False
    return True

number = 0

for a in range(-999,1001,2):
    for b in range(a,1001):
        pass
