#!/usr/bin/env python3

def main():
    b = 1
    # use the formula given in A000984
    for i in range(20):
        b = b*(4*i+2)//(i+1)
    print(b)

if __name__ == '__main__':
    main()

# 0.106 seconds
