from math import *
from collections import *
from sys import *
from os import *

# Read input as specified in the question.
# Print output as specified in the question.
''' using recursion
num = int(input())

# print(num)


def fibonacciNum(a):
    if a == 2 or a == 1:
        return 1
    return fibonacciNum(a-1) + fibonacciNum(a-2)


print(fibonacciNum(num))
'''

# using loops

num = int(input())
arr = list(range(0, num+1))

# print(arr)
arr[0], arr[1] = 0, 1


def fibonacci_num(val):
    if val <= 1:
        return 1
    for i in range(2, val+1):
        arr[i] = arr[i-2] + arr[i-1]
    return arr[val]


print(fibonacci_num(num))



