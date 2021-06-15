#!/usr/bin/env python
# This program generates Fibonacci numbers 
import sys

def fib(cnt):
  first = 0
  second = 1
  print(first)
  print(second)
  num = 3
  while num <= cnt:
    next = first + second
    first = second
    second = next
    print(second)
    num += 1
  return

fib(int(sys.argv[1]))
