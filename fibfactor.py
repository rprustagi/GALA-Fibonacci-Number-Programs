#!/usr/bin/env python
# This program generates golden ratio 
# It makes of Fibonacci numbers with initial random numbers
import sys
import random

# generate nth Fibonacci numbers
def fib(n):
  if n==0 or n==1:
    return n
  prev = 0
  curr = 1
  cnt = 2
  while cnt <= n:
    next = prev + curr
    prev = curr
    curr = next
    cnt += 1
  return curr

#--------------------
# check if Fib(n) divides Fib(n*i) for i <=k
def fibfactor(n, k):
  fibn = fib(n)
  print("fib({})={}".format(n, fibn))
  cnt = 2
  while cnt <= k:
    fibnk = fib(n*cnt)
    print("fib({},{})={}".format(n,cnt,fibnk))
    if fibnk % fibn != 0:
      return False
    cnt += 1
  return True

print(fibfactor(int(sys.argv[1]), int(sys.argv[2])))
