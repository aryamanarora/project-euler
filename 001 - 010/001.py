#!/usr/bin/env python3
# Finds the sum of all the multiples of 3 or 5 below 1000.

import sys                                      # standard sys module

def main():
    sum = 0                                     # initialize sum
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:            # if i is divisible by 3 or 5...
            sum += i                            # then add to sum
    print(sum)                                  # print sum

if __name__ == '__main__':                      # call main
    main()
