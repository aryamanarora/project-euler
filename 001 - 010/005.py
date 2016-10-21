#!/usr/bin/env python3

import sys

def main():
    result = 2520
    for i in range(11, 21):
        if result % i != 0:
            result = lcm(i, result)
    print(result)
    pass

def lcm(a, b):
    for i in range(b, a*b):
        if i % b == 0 and i % a == 0:
            return i
    return a * b

if __name__ == '__main__':                      # call main
    main()
