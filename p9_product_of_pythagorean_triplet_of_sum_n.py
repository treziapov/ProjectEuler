# A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
import time_tools


def brute_force_pythagorean_triplet_of_sum(n):
    '''
    Calculates the pythagorean triplet of provided sum by iterating
    through all distinct values for 3 numbers and checking each triplet
    '''
    for i in range(1, n // 3):
        for j in range(i + 1, n // 2):
            k = n - i - j
            if is_pythagorean_triplet(i, j, k):
                triplet_sum = sum([i, j, k])
                if triplet_sum == n:
                    return (i, j, k, i * j * k)
    return None


def optimized_pythagorean_triplet_of_sum(n):
    '''
    Calculates the pythagorean triplet of provided sum by using
    a derived formula:

    a^2 + b^2 = c^2
    a + b + c = 1000
    
    ->  a + b + sqrt(a^2 + b^2) = 1000  
    ->  a^2 + b^2 = (1000 - a - b)^2
    ->  a^2 + b^2 = 1000000 - 1000a - 1000b - 1000a + a^2 - ab - 1000b - ab - b^2
    ->  a^2 + b^2 = 1000000 - 2000a - 2000b + 2ab + a^2 + b^2
    ->  0 = 1000000 - 2000(a + b) + 2ab
    ->  2000a + 2000b - 2ab = 1000000
    -> ...
    -> a = (500000 - 1000b) / (1000 - b)
    '''
    for b in range(1, n // 2):
        a = (500000 - 1000 * b) / (1000 - b)
        if a % 1 == 0:
            a = int(a)
            c = n - a - b
            return (a, b, c, a * b * c)
    return None


def is_pythagorean_triplet(a, b, c):
    '''
    Determines if the provided 3 arguments (in asecnding order)
    are a pythagorean triplet, which must satify the following equation:

    a^2 + b^2 = c^2
    '''
    return a*a + b*b == c*c


def main():
    '''
    There exists exactly one Pythagorean triplet for which a + b + c = 1000
    Find the product abc

    Answer: 31875000
    '''
    n = 1000
    args = [n]

    f = brute_force_pythagorean_triplet_of_sum
    time_tools.time_func(f, args, 'Brute force')

    f = optimized_pythagorean_triplet_of_sum
    time_tools.time_func(f, args, 'Optimized')


if __name__ == "__main__":
    main()
