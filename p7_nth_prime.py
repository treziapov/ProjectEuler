# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13

# What is the 10 001st prime number?
import time_tools


def brute_force_nth_prime(n):
    '''
    Computes the n'th prime by keeping track of current primes
    '''
    primes = set()

    def is_prime(i):
        '''
        Determines if number n is prime based on previous primes
        '''
        result = True
        if i in primes:
            return False
        for p in primes:
            if i % p == 0:
                return False
        return True

    current = 2

    while True:
        is_n_prime = is_prime(current)
        if is_n_prime:
            primes.add(current)
            n = n - 1
            if n == 0:
                return current
        current = current + 1


def main():
    '''
    What is the 10 001st prime number?

    Answer: 104743
    '''
    n = 10001
    args = [n]
    time_tools.time_func(brute_force_nth_prime, args, "Brute force")


if __name__ == "__main__":
    main()
