#!/usr/bin/env python
# This program generates Fibonacci numbers 
# Outouts last N digits and identifies a repeating pattern
import sys
import re

def fib(cnt,lastNdigits):
  first = 0
  second = 1
  digitstr = ""
  digitstr += str(first)
  digitstr += str(second)
  num = 3
  while num <= cnt:
    next = first + second
    first = second
    second = next
    digitstr += str(second % 10**lastNdigits)
    num += 1
  print(digitstr)
  regex = re.compile(r"(.+?)\1+")
  pattern = regex.match(digitstr)
  print("cycle Length of repeating pattern=",len(pattern.group(1))//lastNdigits)
  print(pattern.group(1))
  return

fib(int(sys.argv[1]), int(sys.argv[2]))
