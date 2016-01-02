# The four adjacent digits in the 1000-digit number that have the
# greatest product are 9 x 9 x 8 x 9 = 5832

# Find the thirteen adjacent digits in the 1000-digit number that
# have the greatest product. What is the value of this product?
import time_tools
import operator


def brute_force_n_adjacent_digits_with_greatest_product(n, s):
    '''
    Determines the n adjacent digits in the given number with the
    greatest product

    The algorithm iterates the whole number string keeping track of
    the local maximum
    '''
    current_string = None
    current_numbers = None
    current_product = None
    current_max = (0, None)

    max_index = len(s) - n - 1
    for i in range(0, max_index):
        current_string = s[i : i + n]
        current_numbers = [int(c) for c in current_string]
        current_product = reduce(operator.mul, current_numbers, 1)
        
        if (current_product > current_max[0]):
            current_max = (current_product, current_numbers)
    return current_max


def optimized_n_adjacent_digits_with_greatest_product(n, s):
    '''
    Determines the n adjacent digits in the given number with the
    greatest product

    The algorithm iterates the whole number string keeping track of
    the local maximum and local products to avoid repetitive work
    '''
    len_s = len(s)
    if len_s < n:
        return None

    current_string = s[0:n]
    current_numbers = [int(c) for c in current_string]
    current_product = reduce(operator.mul, current_numbers, 1)
    current_max = (current_product, current_numbers)

    max_index = len_s - n
    for i in range(0, max_index):
        old_digit = current_numbers[0]
        new_digit = int(s[i+n])
        
        current_string = s[i + 1:i + 1 + n]
        current_numbers = current_numbers[1:] + [new_digit]
        
        if (old_digit != 0):
            current_product = current_product // old_digit
        else:
            current_product = reduce(operator.mul, current_numbers[:-1], 1)
        
        current_product = current_product * new_digit
        
        if (current_product > current_max[0]):
            current_max = (current_product, current_numbers)

    return current_max 


def main():
    '''
    Find the thirteen adjacent digits in the 1000-digit number that
    have the greatest product 

    What is the value of this product?

    Answer: 23514624000
    '''
    n = 13
    s = (
        "73167176531330624919225119674426574742355349194934"
        "96983520312774506326239578318016984801869478851843"
        "85861560789112949495459501737958331952853208805511"
        "12540698747158523863050715693290963295227443043557"
        "66896648950445244523161731856403098711121722383113"
        "62229893423380308135336276614282806444486645238749"
        "30358907296290491560440772390713810515859307960866"
        "70172427121883998797908792274921901699720888093776"
        "65727333001053367881220235421809751254540594752243"
        "52584907711670556013604839586446706324415722155397"
        "53697817977846174064955149290862569321978468622482"
        "83972241375657056057490261407972968652414535100474"
        "82166370484403199890008895243450658541227588666881"
        "16427171479924442928230863465674813919123162824586"
        "17866458359124566529476545682848912883142607690042"
        "24219022671055626321111109370544217506941658960408"
        "07198403850962455444362981230987879927244284909188"
        "84580156166097919133875499200524063689912560717606"
        "05886116467109405077541002256983155200055935729725"
        "71636269561882670428252483600823257530420752963450"
    )
    args = [n, s]
    
    f = brute_force_n_adjacent_digits_with_greatest_product
    time_tools.time_func(f, args, "Brute force")

    f = optimized_n_adjacent_digits_with_greatest_product
    time_tools.time_func(f, args, "Optimized")

if __name__ == "__main__":
    main()
