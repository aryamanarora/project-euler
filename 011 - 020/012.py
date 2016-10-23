#!/usr/bin/env python3

import sys

def main():
    i, j = 1, 1
    while factors(i) < 510:
        print(i, factors(i))
        j += 1
        i += j
    print(i, factors(i))

def factors(num):
    results = 2
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            results += 1
    return results

if __name__ == '__main__':
    main()
