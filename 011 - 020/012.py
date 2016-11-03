#!/usr/bin/env python3

import sys

def main():
    j, i = 1, 1
    results = []
    # generates triangle numbers
    while factornum(i) < 1000:
        i = int((j * (j + 1)) / 2)
        print(i, factornum(i))
        if factornum(i) > 500:
            results.append(i)
        j += 1
    print(results)

# finds the number of factors for a number
def factornum(num):
    primefactors = [0] * (num//2 + 1)
    for i in range(2, num//2 + 1):
        if num % i == 0:
            while num % i == 0:
                num /= i
                primefactors[i] += 1
    result = 1
    for j in primefactors:
        result *= (primefactors[j] + 1)
    return result

if __name__ == '__main__':
    main()
