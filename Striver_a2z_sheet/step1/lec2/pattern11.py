"""
https://www.naukri.com/code360/problems/binary-number-triangle_6581890?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=DISCUSS
Binary Number Triangle
1
0 1
1 0 1
"""


def nBinaryTriangle(n: int) -> None:

    for i in range(1, n+1):
        start: int = i % 2

        for j in range(i):
            print(start, end=' ')
            start ^= 1
        print()


val: int = int(input())

nBinaryTriangle(val)

