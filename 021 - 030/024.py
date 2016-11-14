def builtins(): # 2.4 seconds
    import itertools as it

    # this one is a bit cheaty, and not very efficient
    r = list(it.permutations(range(10)))
    print(r[999999])

def real(): # 0.07 seconds
    import math

    # finds factoradic of 999999
    num_list, f, i = list(range(10)), [], 9
    num = 999999

    while i >= 0:
        f.append(num // math.factorial(i))
        num %= math.factorial(i)
        i -= 1

    # makes a list of the result
    result = []

    # uses factoradic to select items from a list and find the solution
    for item in f:
        result.append(num_list[item])
        del num_list[item]

    # formats and prints nicely
    print("".join(map(str,result)))

if __name__ == '__main__':
    builtins()
    real()
