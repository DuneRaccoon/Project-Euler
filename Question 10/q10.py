from math import sqrt
    
def get_primes_to(number):
    primes_sieve = [True] * (number + 1)
    for n in range(2, round(sqrt(number)) + 1):
        if primes_sieve[n]:
            for i in range(n * n, number + 1, n):
                primes_sieve[i] = False
    return sum([i for i,e in enumerate(primes_sieve) if e][2:])
