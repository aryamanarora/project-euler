#!/usr/bin/env python3

"""
This one took a while, but is reasonably fast.

| Min Factor | Time   |
| :--------- | :----- |
| 20         | 0.085  |
| 50         | 0.091  |
| 100        | 0.109  |
| 200        | 0.197  |
| 300        | 0.215  |
| 400        | 1.135  |
| 500        | 4.307  |
| 600        | 5.812  |
| 700        | 13.446 |
"""

import sys
from math import sqrt, ceil

def triangle():
    n = 1
    while True:
        yield int((n*(n+1))/2)
        n += 1

def factors(n):
    factors = 1
    if n % 2 == 0:
        for i in range(1, ceil(sqrt(n))):
            if n % i == 0: factors += 2
    return factors

def main():
    for i in triangle():
        # print(i, factors(i))
        if factors(i) > 500:
            print(i, "has", factors(i), "factors.")
            return 0

if __name__ == '__main__':
    main()
