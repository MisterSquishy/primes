import sys
import random

def main(n, k):

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
    assert isinstance(k, long)
    assert n > 2

    # find max power of two that divides n-1, and the factor of n-1 by which it divides
    max_power_of_2, non_two_factor = 0, n - 1
    while non_two_factor % 2 == 0:
        max_power_of_2 += 1
        non_two_factor /= 2

    for _ in xrange(k):
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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # a 200 digit prime, neato!
        n = 58021664585639791181184025950440248398226136069516938232493687505822471836536824298822733710342250697739996825938232641940670857624514103125986134050997697160127301547995788468137887651823707102007839
        k = 40
    elif len(sys.argv) == 2:
        n, k = sys.argv[1], 40
    else:
        n, k = sys.argv[1], sys.argv[2]
    print main(long(n), long(k))