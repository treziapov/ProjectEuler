import math

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?


def prime_factors_by_trial_division(n):
    '''
    Trial division by prime numbers
    '''
    if n < 2:
        return []
    prime_factors = []
    max_factor = math.floor(math.sqrt(n))
    for p in prime_sieve_eratosthenes(max_factor):
        if p * p > n:
            break
        while n % p == 0:
            prime_factors.append(p)
            n = int(n / p)
    if n > 1:
        prime_factors.append(n)
    return prime_factors


def prime_sieve_eratosthenes(n):
    '''
    Eratosthenes algorithm to generate prime numbers less than n
    O(nloglogn) runtime
    O(n) space
    '''
    max_factor = math.floor(math.sqrt(n))
    prime_candidates = {}
    for i in range(2, max_factor):
        if i not in prime_candidates:
            for j in range(i*i, n, i):
                prime_candidates[j] = False
    primes = [i for i in range(2, n) if i not in prime_candidates]
    return primes


def main():
    '''
    Determine the largest prime factor of the number 600851475143
    '''
    number = 600851475143
    primes = prime_factors_by_trial_division(number)
    print(primes[-1])

if __name__ == "__main__":
    main()
