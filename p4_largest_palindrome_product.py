# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit
# numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
import time
import functools


def is_palindrome_recursive(s):
    '''
    Recursive palindrome check
    '''
    if len(s) == 0:
        return True
    return s[0] == s[-1] and is_palindrome_recursive(s[1:-1])


def is_palindrome_iterative(s):
    '''
    Iterative palindrome check
    '''
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True


def is_palindrome_string_reverse(s):
    '''
    String reversal palindrome check
    '''
    return s == s[::-1]


def brute_force_largest_palindrome_product(palindrome_func, num_digits):
    '''
    Brute force algorithm to calculate largest palindrome product
    for given number of digits
    '''
    start = 10 ** (num_digits - 1)
    end = 10 ** num_digits
    current_max_product = (0, None, None)
    for i in range(start, end):
        for j in range(start, end):
            candidate = i * j
            candidate_str = str(candidate)
            is_palindrome = palindrome_func(candidate_str)
            if is_palindrome and candidate > current_max_product[0]:
                current_max_product = (candidate, i, j)
    return current_max_product


def optimized_largest_palindrome_product(palindrome_func, num_digits):
    '''
    Optimized brute force algorithm
    '''
    start = 10 ** (num_digits - 1)
    end = 10 ** num_digits
    current_max_product = (0, None, None)
    for i in range(start, end):
        for j in range(i, end):
            candidate = i * j
            candidate_str = str(candidate)
            if candidate > current_max_product[0]:
                is_palindrome = palindrome_func(candidate_str)
                if is_palindrome:
                    current_max_product = (candidate, i, j)
    return current_max_product


def time_palindrome(func, start, end, description):
    start = time.time()
    for i in range(1000, 100000):
        func(str(i))
    elapsed = time.time() - start
    print('{desc}: {sec} seconds'.format(desc=description, sec=elapsed))


def time_largest_palindrome_product(func, num_digits, description):
    start = time.time()
    result = func(num_digits)
    elapsed = time.time() - start
    print('{desc}: {sec} seconds'.format(desc=description, sec=elapsed))
    print(result)


def main():
    '''
    Find the largest palindrome made from the product of two 3-digit numbers

    Answer: 906609 = 913 * 993
    '''
    # Palindrome check time tests
    start = 1000
    end = 1000000
    time_palindrome(is_palindrome_recursive, start, end, 'Recursive')
    time_palindrome(is_palindrome_iterative, start, end, 'Iterative')
    time_palindrome(is_palindrome_string_reverse, start, end, 'String reverse')

    # Largest palindrome product time tests
    num_digits = 4
    p = is_palindrome_string_reverse
    f_brute = functools.partial(brute_force_largest_palindrome_product, p)
    f_optimized = functools.partial(optimized_largest_palindrome_product, p)
    time_largest_palindrome_product(f_brute, num_digits, 'Brute force')
    time_largest_palindrome_product(f_optimized, num_digits, 'Brute force')


if __name__ == "__main__":
    main()
