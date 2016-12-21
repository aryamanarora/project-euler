#!/usr/bin/env python3

values = 100000 # adjust this
# def triangle():
#     n = 1
#     while n < values:
#         yield int((n*(n+1))/2)
#         n += 1

def pentagon():
    n = 1
    while n < values:
        yield (n*(3*n-1))//2
        n += 1

def hexagon():
    n = 1
    while n < values:
        yield n*(2*n-1)
        n += 1

def main():
    pent, hexa = [], []
    # tri = []
    # for i in triangle():
    #     tri.append(i)
    for j in pentagon():
        pent.append(j)
    for k in hexagon():
        hexa.append(k)

    print(set(pent).intersection(hexa))

if __name__ == '__main__': # 0.311 seconds!
    main()
