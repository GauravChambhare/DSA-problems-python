"""
https://www.geeksforgeeks.org/problems/count-digits5716/1
"""


def evenlyDivides(n):
    # first create a list containing int digits of num n
    """
    digits = [int(d) for d in str(n)]
    count = sum(1 for d in digits if d != 0 and n % d == 0)
    return count
    """
    # another method is
    copy = n
    count = 0

    while copy > 0:
        digit = copy % 10
        if digit != 0 and n % digit == 0:
            count += 1
        copy //= 10
    return count


n = int(input())
print(evenlyDivides(n))
