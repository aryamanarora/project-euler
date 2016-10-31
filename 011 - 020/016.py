#!/usr/bin/env python3

import sys

def main():
    num = str(int(2**1000))
    result = sum([int(char) for char in num])
    print(result)

if __name__ == '__main__':
    main()

# time : ~0.2 seconds
