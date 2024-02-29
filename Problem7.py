# Problem 7
# https://projecteuler.net/problem=7
from math import log



def upperBoundOfPrimes(n):
    # Mathmatical formula for uppper bound of finding the nth prime number
    if (n < 6):
        return 100
    upperBound = n * (log(n) + log(log(n)))
    return int(upperBound+1)


def sieveOfErosthenes(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False
    for (i, is_prime) in enumerate(prime):
        if is_prime:
            yield i
            for a in range(i*i, n+1, i):
                prime[a]=False
                
answer = int(input("What prime number would you like to find: "))

def find_n_prime(n):
    primes = list(sieveOfErosthenes(upperBoundOfPrimes(n)))
    return primes[n-1]

print(find_n_prime(answer))
