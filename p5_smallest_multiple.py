# 2520 is the smallest number that can be divided by each
# of the numbers from 1 to 10 without any remainder

# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?
import time
import itertools
import p3_largest_prime_factor


def brute_force_smallest_multiple(numbers):
    '''
    Brute force algorithm to find smallest common multiple
    '''
    i = 1
    while True:
        is_multiple = is_common_multiple(i, numbers)
        if not is_multiple:
            i = i + 1
            continue
        return i


def optimized_brute_force_smallest_multiple(numbers):
    '''
    Intuitively optimized brute force algorithm
    '''
    max_num = max(numbers)
    i = max_num
    while True:
        is_multiple = is_common_multiple(i, numbers)
        if not is_multiple:
            i = i + max_num
            continue
        return i


def optimized_smallest_multiple(numbers):
    '''
    Optimized solution
    '''
    needed_prime_factors = {}
    for n in numbers:
        primes = prime_factors(n)
        for p, g in itertools.groupby(primes, key=lambda x: x):
            l = list(g)
            new = p not in needed_prime_factors
            if new:
                needed_prime_factors[p] = l
                continue
            more_copies = len(l) > len(needed_prime_factors[p])
            if more_copies:
                needed_prime_factors[p] = l
                continue

    multiple = 1
    for n, l in needed_prime_factors.items():
        multiple = multiple * (n**len(l))
    return multiple


def prime_factors(n):
    f = p3_largest_prime_factor.prime_factors_by_trial_division
    primes = f(n)
    return primes


def is_common_multiple(n, numbers):
    '''
    Determines if the number n is a common multiple for given numbers
    '''
    for num in numbers:
        if n % num != 0:
            return False
    return True


def time_func(func, args, description):
    '''
    Timing wrapper
    '''
    start = time.time()
    result = func(args)
    elapsed = time.time() - start
    print('Result: {result}'.format(result=result))
    print('{desc}: {sec} seconds'.format(desc=description, sec=elapsed))


def main():
    '''
    What is the smallest positive number that is evenly
    divisible by all of the numbers from 1 to 20?

    Answer: 232792560
    '''
    numbers = range(1, 21)
    # time_func(brute_force_smallest_multiple, numbers, 'Brute force')
    # time_func(optimized_brute_force_smallest_multiple, numbers,
    #     'Optimized brute force')
    time_func(optimized_smallest_multiple, numbers, 'Optimized')

if __name__ == "__main__":
    main()
