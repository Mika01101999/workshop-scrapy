#!/usr/bin/env python3

import sys
import math

def isAnagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    if (str1_list == str2_list):
        print("anagram")
    else:
        print("not anagram")

if __name__ == '__main__':
    isAnagram(sys.argv[1], sys.argv[2])
    