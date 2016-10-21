#!/usr/bin/env python3

import sys
import math

def main():
    (m, n, result) = 0, 0, 0
    while m < 1000:
        while n < m:
            if m*(m + n) == 500:
                print((m**2 - n**2) * (2*m*n) * (m**2 + n**2))
            n += 1
        n = 0
        m += 1

if __name__ == '__main__':
    main()
