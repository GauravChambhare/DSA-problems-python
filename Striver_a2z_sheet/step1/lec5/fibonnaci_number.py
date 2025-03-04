"""
https://leetcode.com/problems/fibonacci-number/description/
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
"""


from functools import lru_cache
@lru_cache(maxsize=None)

def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


k = int(input("Enter a int: "))
print(fib(k))


