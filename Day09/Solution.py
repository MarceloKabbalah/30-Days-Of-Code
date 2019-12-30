#!/bin/python
# compatible with python3

def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

n = int(input())
print(factorial(n))