# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9
# The sum of these multiples is 23


def multiples_of(factors, cap):
    '''
    Returns a list of natural numbers that are multiples of given factors
    under the cap
    '''
    multiples = set()
    current_multiples = factors

    while True:
        some_multiple_within_cap = False

        for multiple in current_multiples:
            if (multiple < cap and multiple != 0):
                multiples.add(multiple)
                some_multiple_within_cap = True

        if not some_multiple_within_cap:
            break
        else:
            current_multiples = [
                current_multiples[i] + factor
                for i, factor in enumerate(factors)
            ]

    result = list(multiples)
    return result


def multiples_of_short(factors, cap):
    '''
    Returns a list of natural numbers that are multiples of given factors
    under the cap
    Shorter but not optimal solution
    '''
    multiples = [
        i for i in range(1, cap) 
        if any(i % f == 0 for f in factors)
    ]
    return multiples


def main():
    '''
    Find the sum of all the multiples of 3 or 5 below 1000
    Answer: 233168
    '''
    factors = [3, 5]
    cap = 1000
    
    multiples = multiples_of(factors, cap)
    result = sum(multiples)
    print(result)

    multiples = multiples_of_short(factors, cap)
    result = sum(multiples)
    print(result)


if __name__ == "__main__":
    main()
