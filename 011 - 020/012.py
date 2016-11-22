#!/usr/bin/env python3

"""
This one took a while, but is reasonably fast.

| Min Factor | Even   | All    |
| :--------- | :----- | :----- |
| 20         | 0.085  | 0.070  |
| 50         | 0.091  | 0.074  |
| 100        | 0.109  | 0.069  |
| 200        | 0.197  | 0.250  |
| 300        | 0.215  | 0.232  |
| 400        | 1.135  | 1.552  |
| 500        | 4.307  | 6.095  |
| 600        | 5.812  | 8.279  |
| 700        | 13.446 | 18.390 |
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
    else:
        for i in range(1, ceil(sqrt(n)), 2):
            if n % i == 0: factors += 2
    return factors

def main():
    for i in triangle():
        # print(i, factors(i))
        if factors(i) > 700:
            print(i, "has", factors(i), "factors.")
            return 0

if __name__ == '__main__':
    main()
