#!/usr/bin/env python
# This program generates golden ratio 
# It makes of Fibonacci numbers with initial random numbers
import sys
import random

def goldenratio(cnt):
  first = random.randint(1,100)
  second = random.randint(1,100)
  num = 3
  while num <= cnt:
    next = first + second
    first = second
    second = next
    num += 1
  return second/first

print(goldenratio(int(sys.argv[1])))
