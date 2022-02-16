#!/usr/bin/env python3

import sys
import math

def ex01():
    for i in range(101):
        if (i % 3 ==0 and i % 5 ==0):
            print("ThreeFive")
        elif(i % 5 ==0):
            print("Five")
        elif(i % 3 ==0):
            print("Three")
        else:
            print(i)
    return 0

if __name__ == '__main__':
    ex01()