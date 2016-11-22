#!/usr/bin/env python3
import inflect

def main():
    result = 0
    p = inflect.engine()
    for i in range(1,1001):
        string = p.number_to_words(i, andword='and').replace(" ","")
        string = string.replace("-","")
        result += len(string)
    print(result)

if __name__ == '__main__':
    main()
