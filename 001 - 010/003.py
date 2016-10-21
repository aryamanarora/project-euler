#!/usr/bin/env python3

import sys

def main(argv):
    num = int(argv[1])                          # remember the input as an int

    while num % 2 == 0:                         # while the number is even ...
        num /= 2                                # divide it by 2 ...
        print("2")                              # and print 2, because it is a factor

    i = 3                                       # next factor to check ...

    while num != 1:                             # while the number still has factors
        while num % i == 0:                     # while the number is divisible by i ...
            num /= i                            # divide it by i
            print(i)                            # print i because it is a factor
        i += 2                                  # try next non-even factor

    pass

if __name__ == '__main__':                      # call main
    main(sys.argv)
