# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025 − 385 = 2640

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum
import time_tools


def brute_force_sum_square_difference(numbers):
    '''
    Brute force solution to calculate sum square difference
    '''
    sum_of_squares = 0
    square_of_sum = 0
    for n in numbers:
        sum_of_squares = sum_of_squares + n**2
        square_of_sum = square_of_sum + n
    square_of_sum = square_of_sum**2
    diff = abs(sum_of_squares - square_of_sum)
    return diff


def optimal_sum_square_difference(numbers):
    '''
    Optimal solution to calculate sum square difference
    Note:
        Assumes numbers make up a contigious range starting from 1
    '''
    n = numbers[-1]

    sum_squared = (n * (n + 1) // 2) ** 2
    square_sum = (n * (n + 1) * (2 * n + 1)) // 6

    result = sum_squared - square_sum
    return result


def main():
    '''
    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum

    Answer: 25164150
    '''
    numbers = range(1, 101)
    args = [numbers]
    time_tools.time_func(brute_force_sum_square_difference, args, 'Brute force')
    time_tools.time_func(optimal_sum_square_difference, args, 'Optimized')

if __name__ == "__main__":
    main()
