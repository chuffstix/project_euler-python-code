'''
Various tools to generate and factorise prime numbers
'''

import math


def psieve():
    """
    The following code pasted from
    https://stackoverflow.com/questions/2211990/
    how-to-implement-an-efficient-infinite-generator
    -of-prime-numbers-in-python/10733621#10733621
    for a very efficient prime generator
    """
    import itertools
    yield from (2, 3, 5, 7)
    D = {}
    ps = psieve()
    next(ps)
    p = next(ps)
    assert p == 3
    psq = p * p
    for i in itertools.count(9, 2):
        if i in D:  # composite
            step = D.pop(i)
        elif i < psq:  # prime
            yield i
            continue
        else:  # composite, = p*p
            assert i == psq
            step = 2 * p
            p = next(ps)
            psq = p * p
        i += step
        while i in D:
            i += step
        D[i] = step


def prime_dict_generator(max: int):
    prime_dict = {}
    for i in range(2, max):
        prime_dict[i] = True  # create dict of all positive integers marked as prime
    for i in range(2, max):
        if prime_dict[i] == True:  # if key is prime - (starts at 2 so first entry is already prime...)
            for j in range(i*2, max, i):  # j is multiples of i, starting from i*2
                prime_dict[j] = False
    for i in range(2, max):
        try:
            if prime_dict[i] == False:
                del prime_dict[i]
        except:
            continue  # catch the error raised when prime_dict[i] doesn't exist
    return prime_dict.keys()
#prime_dict_generator(40)


def prime_factors(num: int) ->list:
    factors_list = []
    while num % 2 == 0:
        factors_list.append(2)
        num /= 2
    for i in range(3, int(math.sqrt(num))+1, 2):
        while num % i == 0:
            factors_list.append(i)
            num /= i
    if num > 2:
        factors_list.append(num)
    return factors_list


def largest_prime_factor(num):
    factors_list = prime_factors(num)
    return str(factors_list[-1:])[1:-1]

#largest_prime_factor(600851475143)
#print(prime_factors(120))