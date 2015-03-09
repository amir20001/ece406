#!/usr/bin/env python3
"""
ECE 406, Winter 2015:  File for Exercise 1 of Assignment #3 
"""
import numpy.fft as np


def main():
    """
    Exercise 1:  Using the FFT to multiply two binary numbers.  
    You just need to fill in parts (v) and (vi)
    """
    # The binary numbers and their product
    a_bin = 0b1001001001
    b_bin = 0b1010101010
    c_bin = a_bin * b_bin
    print('The product of a and b is', c_bin)


    # (i) The coefficients of the polynomials A and B
    Acoeff = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
    Bcoeff = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]


    # (ii) the value representations of A and B
    Aval = np.fft(Acoeff, 32)
    Bval = np.fft(Bcoeff, 32)


    # (iii) The value representation of C
    Cval = []
    for i in range(len(Aval)):
        Cval.append(Aval[i] * Bval[i])


    # (iv) The coefficients of the polynomial C
    Ccoeff = np.ifft(Cval)
    # we'll get rid of the imaginary parts, which are just numerical errors
    for i, c in enumerate(Ccoeff):
        Ccoeff[i] = int(round(c.real))


    # (v) calculate the product by evaluating the polynomial at 2, i.e., C(2)
    # (You may need to take the real part at the end if there is a small imaginary component)
    prod = 0
    for i in range(len(Ccoeff)):
        prod += int(round(Ccoeff[i].real)) * (2 ** i)

    print('Using the FFT the product of a and b is', int(round(prod.real)))
    # (vi) write code to calculate the binary digits of c directly from the coefficients of C, Ccoeff.
    # hint:  You can use (q,r) = divmod(x, 2) to find the quotient and remainder of x when divided by 2
    q = 0
    binaryArray = []
    for i in range(len(Ccoeff)):
        real = int(round(Ccoeff[i].real)) + q
        (q, r) = divmod(real, 2)
        binaryArray.append(r)
    binaryArray.reverse()
    print("binary value of c: ", binaryArray)


if __name__ == '__main__':
    main()
