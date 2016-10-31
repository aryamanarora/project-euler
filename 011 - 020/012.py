#!/usr/bin/env python3

import sys

def main():
    j, i = 1, 1
    # generates triangle numbers
    while factors(i) < 1000:
        i = int((j * (j + 1)) / 2)
        print(i, factors(i))
        if factors(i) > 500:
            print(i, factors(i))
            pass
        j += 1

# finds the number of factors for a number
def factors(num):
    num = int(num)
    results = 2
    # optimization for odd numbers; only check for odd factors
    if num % 2 == 0:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                results += 1
    else:
        for i in range(3, num // 2, 2):
            if num % i == 0:
                results += 1
    return results

if __name__ == '__main__':
    main()
