import eulerlib
import itertools


list_of_primes = []
i = 0
while len(list_of_primes) < 10001:
    i += 1
    if eulerlib.prime_numbers.is_prime(i):
        list_of_primes.append(i)

print(list_of_primes[-1])
