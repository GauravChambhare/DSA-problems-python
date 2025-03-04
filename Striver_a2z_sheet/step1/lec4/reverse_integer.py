'''
https://leetcode.com/problems/reverse-integer/
'''


def reverse(x: int) -> int:
    # reversed in should be within 32-bit memory range if it gets out of range return 0
    # also
    sign = 1 if x >= 0 else -1
    # print(sign)
    rev = (int(str(abs(x))[::-1]))* sign
    if 2**31> rev >= -2**31:
        return rev
    else:
        return 0
    """Another method
    flag = False
    if x <0:
        flag = True
        x = abs(x)

    num = [d for d in str(x)]
    # print(num)
    rev = "".join(reversed(num))
    rev = int(rev)
    if flag:
        rev = -rev
    # print(type(rev))
    if 2 ** 31 > rev >= -2 ** 31:
        # print(rev)
        return rev
    else:
        return 0
    """

x = int(input())
print(reverse(x))