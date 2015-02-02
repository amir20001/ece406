#!/usr/bin/env python3
"""
Assignment 2 Python file
Cut-and-paste (or import) your extended_euclid and modexp functions
from assignment 1
"""
import random
import math



# part (i) for modular exponentiation
def modexp(x, y, N):
    """
    Input: Three positive integers x and y, and N.
    Output: The number x^y mod N
    """
    if y == 0:
        return 1
    z = modexp(x, math.floor(y / 2), N)
    if y % 2 == 0:
        return (z * z) % N
    else:
        return (x * z * z) % N


# part (ii) for extended Euclid
def extended_euclid(a, b):
    """
    Input: Two positive integers a >= b >= 0
    Output: Three integers x, y, and d returned as a tuple (x, y, d)
            such that d = gcd(a, b) and ax + by = d
    """

    if b == 0:
        return 1, 0, a
    (x_new, y_new, d) = extended_euclid(b, a % b)

    return y_new, x_new - math.floor(a / b) * y_new, d


def primality(N):
    """
    Test if a number N is prime using Fermat's little Theorem with
    ten random values of a.  If a^(N-1) mod N = 1 for all values,
    then return true.  Otherwise return false.
    Hint:  you can generate a random integer between a and b using
    random.randint(a,b).
    """
    if N <= 3:
        return True
    for i in range(10):
        a = random.randint(1, N - 1)
        if modexp(a, N - 1, N) != 1:
            return False
    return True


def prime_generator(N):
    """
    This function generates a prime number <= N
    """
    while True:
        rand = random.randint(1, N)
        if primality(rand):
            return rand
    return 0


def generate_values():
    while True:
        p = prime_generator(10000000)
        # verify p is 7 digits
        if len(str(p)) < 7:
            continue
        q = prime_generator(10000000)
        # verify q is 7 digits
        if len(str(q)) < 7:
            continue
        N = p * q
        n = (p - 1) * (q - 1)
        e = 5
        if n % 5 == 0:
            # make sure n is coprime with e
            continue
        (x, y, r) = extended_euclid(e, n)
        # make sure that the modular inverse exists
        if r == 1:
            print("p", p)
            print("q", q)
            print("p-1*q-1", n)
            return N, e, (x % n)


def main():
    """
    Test file for the two parts of the question
    """
    ##################
    ## Excercise 1:  generating primes and RSA

    (N, public, private) = generate_values()
    print("public", public)
    print("private", private)
    print("N", N)
    x = 101010
    enc = modexp(x, public, N)
    print("enc", enc)
    dec = modexp(enc, private, N)
    print("dec", dec)


if __name__ == '__main__':
    main()
