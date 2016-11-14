#!/usr/bin/env python3

def main():
    print(one,two,six,ten)
    result = 0
    for i in range(1,1001):
        if i in (1,2,6,10):
            result += 3
        elif i in (4,5,9):
            result += 4
        elif i in (3,7,8):
            result += 5
        elif i in (11,12):
            result += 6
        elif i in (15,16):
            reult += 7
        elif i in (13,14,18,19):
            result += 8
        elif i == 17:
            result += 9
    print(result)

if __name__ == '__main__':
    main()
