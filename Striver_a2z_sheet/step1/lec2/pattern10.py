"""
https://www.naukri.com/code360/problems/rotated-triangle_6573688?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SUBMISSION
 Rotated Triangle
*
**
***
**
*

"""


def nStarTriangle(n: int) -> None:
    # Write your code here.

    for row in range(n):
        for pat in range(row+1):
            print('*', end="")
        print()
    for row in range(n-1, 0, -1):
        for pat in range(row):
            print('*', end="")
        print()


val: int = int(input())

nStarTriangle(val)
