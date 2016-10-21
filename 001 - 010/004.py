#!/usr/bin/env python3

import sys

def main():
    answer = 10000
    for i in range(900, 999):
        for j in range(900, 999):
            if i*j == reverse_num(i*j) and i*j > answer:
                answer = i * j
    print(answer)
    pass

def reverse_num(num):
    reverse = 0
    while num > 0:
        reverse = reverse * 10 + (num % 10)
        num //= 10
    return reverse

if __name__ == '__main__':                      # call main
    main()
