#!/usr/bin/env python3
# Finds the sum of the even Fibonacci numbers that are less than 4 million.

import sys                                      # standard sys module

def main():
    (term0, term1) = 1, 2                       # first two Fibonacci terms
    termsum = 0                                 # initialize termsum
    for i in range(2, 10000):                   # 10000 iterations max
        if term1 % 2 == 0 and term1 < 4000000:  # if term1 is even and less than 4 million ...
            termsum += term1                    # then add it to termsum
        elif term1 >= 4000000:                  # if we go beyond 4 million ...
            break                               # stop!
        term1 = term1 + term0                   # next term
        term0 = term1 - term0                   # term0 is now old term1
    print(termsum)                              # we're done folks!

if __name__ == '__main__':                      # call main
    main()
