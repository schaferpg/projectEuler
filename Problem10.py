# Problem 10
# https://projecteuler.net/problem=10
# Reused sieve from problem 7
def sieveOfErosthenes(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False
    for (i, is_prime) in enumerate(prime):
        if is_prime:
            yield i
            for a in range(i*i, n+1, i):
                prime[a]=False
                
answer = int(input("Find the sum of all primes below: "))
def sum_Of_Primes(n):
    primes = list(sieveOfErosthenes(n))
    total = 0
    for p in primes:
        total += p
    return total

print(sum_Of_Primes(answer))
