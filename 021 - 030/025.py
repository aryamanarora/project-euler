#!/usr/bin/env python3

import sys

def main():
    i, num1, num2, num = 2, 1, 1, 2
    while len(str(num)) <= 1000:
        num = num1 + num2
        i += 1
        if len(str(num)) == 1000:
            print(i, num, "Length:", len(str(num)))
        num1 = num2
        num2 = num

if __name__ == '__main__':
    main()
