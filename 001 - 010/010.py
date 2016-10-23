#!/usr/bin/env python3

import sys
import math

def main():
    sum = 0
    for i in range(2000001):
        if isprime(i) == True:
            print(i)
            sum += i
    print(sum)
    pass

def isprime(num):
    if num == 2:
        return True
    elif num % 2 == 0 or num == 1:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()
