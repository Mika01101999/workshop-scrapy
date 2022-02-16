#!/usr/bin/env python3

import sys
import math

def colorful(n):
        temp = []
        hashlist = {}
        s = str(n)
        for i in range(len(s)):
            for j in range(i, len(s)):
                temp.append(s[i:j + 1])
        for l in range(len(temp)):
            mx = 1
            p = temp[l]
            for k in range(len(p)):
                mx *= int(p[k])
            hashlist[p] = mx
        temp0 = []
        for k, v in hashlist.items():
            if v not in temp0:
                temp0.append(v)
        if len(temp0) == len(temp):
            print ("true")
            return 1
        else:
            print ("false")
            return 0


if __name__ == '__main__':
    colorful(sys.argv[1])
    