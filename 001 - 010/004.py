#!/usr/bin/env python3

import sys

def main():
    answer = 10000
    for i in range(100, 1000):
        for j in range(100, 1000):
            if i*j == int(str(i*j)[::-1]) and i*j > answer:
                answer = i * j
    print(answer)

if __name__ == '__main__':                      # call main
    main()
