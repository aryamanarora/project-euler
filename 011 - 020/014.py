#!/usr/bin/env python3

import sys

def main():
    result = 0
    for num in range(1,1000000):
        collatz = 0
        original = num
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num = 3*num + 1
            collatz += 1
        if collatz > result:
            result = collatz
            print(original, collatz)

if __name__ == '__main__':
    main()

# 44.051 seconds
