import sys
import random
import math
from mpmath import mp
import fractions

def is_probably_prime(n):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification
    #
    # FORKED FROM https://gist.github.com/Ayrx/5884790
    #
    # Some hundred-digit primes for testing: https://primes.utm.edu/lists/small/small2.html
    # Good large primes for factoring: https://asecuritysite.com/encryption/random3


    # validate input
    assert isinstance(n, long)
    assert n > 2

    # find max power of two that divides n-1, and the factor of n-1 by which it divides
    max_power_of_2, non_two_factor = 0, n - 1
    while non_two_factor % 2 == 0:
        max_power_of_2 += 1
        non_two_factor /= 2

    for _ in xrange(40):
        # get a random between 2 and n - 2
        a = random.randrange(2, n - 1)
        random_2_to_n_minus_2 = pow(a, non_two_factor, n)
        if random_2_to_n_minus_2 == 1 or random_2_to_n_minus_2 == n - 1:
            continue

        # keep taking even powers of the rando and modding by n
        # if we have to try more than max power of 2 - 1 times before reaching n-1, this number isn't prime  
        for _ in xrange(max_power_of_2 - 1):
            random_2_to_n_minus_2 = pow(random_2_to_n_minus_2, 2, n)
            if random_2_to_n_minus_2 == n - 1:
                break
        else:
            return False
    return True

def print_percentage_bar(x, n):
    percentage = (x/float(n))*100
    sys.stdout.write("\r[")
    for i in range(int(percentage)/2):
        sys.stdout.write("=")
    for i in range(50-(int(percentage)/2)):
        sys.stdout.write(" ")
    sys.stdout.write("] "+str(int(percentage))+"%")    

def fact_in_range(n, range):
    primefact = 1
    for x in range:
        print_percentage_bar(x, len(range)) #todo so this is way too slow
        if(is_probably_prime(long(x))):
            primefact *= x
    return fractions.gcd(n, primefact) > 1

def binary_search_factor(n):
    possibleFactors = xrange(5, long(math.ceil(mp.sqrt(n))))
    while len(possibleFactors) > 1:
        print(possibleFactors)
        lowerhalf = xrange(possibleFactors[0], possibleFactors[len(possibleFactors)/2])
        if fact_in_range(n, lowerhalf):
            possibleFactors = lowerhalf
        else:
            possibleFactors = xrange(possibleFactors[len(possibleFactors) / 2], possibleFactors[len(possibleFactors) - 1])
    return possibleFactors

if __name__ == "__main__":
    n = 568911225001276501 #=178127899 * 3193835599
    print(binary_search_factor(n))