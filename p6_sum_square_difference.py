# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025 − 385 = 2640

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum
import time


def brute_force_sum_square_difference(numbers):
    sum_of_squares = 0
    square_of_sum = 0
    for n in numbers:
        sum_of_squares = sum_of_squares + n**2
        square_of_sum = square_of_sum + n
    square_of_sum = square_of_sum**2
    diff = abs(sum_of_squares - square_of_sum)
    return diff


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
    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum

    Answer: 25164150
    '''
    numbers = range(1, 101)
    time_func(brute_force_sum_square_difference, numbers, 'Optimized')

if __name__ == "__main__":
    main()
