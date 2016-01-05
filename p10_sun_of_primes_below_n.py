# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes below two million
import time_tools
import p3_largest_prime_factor as p3


def optimized_sum_of_primes_below(n):
    '''
    Calculates the sum of primes below n by using eratosthenes 
    prime sieve
    '''
    primes = p3.prime_sieve_eratosthenes(n)
    return sum(primes)


def main():
    '''
    Find the sum of all the primes below two million

    Answer: 142913828922
    '''
    n = 2000000
    args = [n]

    f = optimized_sum_of_primes_below
    time_tools.time_func(f, args, 'Optimized')


if __name__ == "__main__":
    main()
