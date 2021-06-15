#!/usr/bin/env python
# The programs to check if a given number is prime number.
import sys

def chkprime(param):
  try:
    num = int(param)
  except:
    return False
  if num == 1:
    return False
  if num == 2:
    return True
  if num % 2 == 0:
    return False
  k = 3
  while k * k <= num:
    if num % k == 0:
      return False
    k = k + 2
  return True

print(chkprime(sys.argv[1]))