import sys

def main():
    result = 2520
    for i in range(11, 21):
        if result % i != 0:
            result = lcm(i, result)
    print(result)
    pass

def lcm(a, b):
    for i in range(int(b), 0, -1):
        if b % i == 0 and a % i == 0:
            return int((a*b)/i)
    return int(a * b)

if __name__ == '__main__':                      # call main
    main()
