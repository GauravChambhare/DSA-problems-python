"""
https://www.naukri.com/code360/problems/number-crown_6581894?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=PROBLEM
Number Crown
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1
"""


def nNumberCrown(val: int) -> None:

    for i in range(1, val+1):
        for j in range(1, i+1):
            print(j, end=" ")
        for k in range(2*(val-i), 0, -1):
            print(" ", end="")
        for l in range(i, 0, -1):
            print(l, end=" ")
        print()


val: int = int(input())

nNumberCrown(val)
