#!/usr/bin/env python3

import sys
import math

def calsum(l):
    return  sum([int(i) for i in l if type(i)== int or i.isdigit()])
  
list1 = ['nothing', 3, '8', 2, '1']
  
print (calsum(list1))
