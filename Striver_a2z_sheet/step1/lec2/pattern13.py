"""
https://www.naukri.com/code360/problems/increasing-number-triangle_6581893?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
Increasing Number Triangle
1
2 3
4 5 6
7 8 9 10
"""


def nNumberTriangle(n: int) -> None:
    # Write your solution here.

    val: int = 1

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(val, end=" ")
            val += 1
        print()


val: int = int(input())

nNumberTriangle(val)
