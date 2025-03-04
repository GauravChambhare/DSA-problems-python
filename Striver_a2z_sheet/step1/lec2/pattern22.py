"""
https://www.naukri.com/code360/problems/ninja-and-the-number-pattern-i_6581959?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=PROBLEM
Ninja And The Number Pattern

33333
32223
32123
32223
33333
"""


def getNumberPattern(n: int) -> None:
    # Write your solution here.

    # min distance from boundaries to be subtracted from value of N to obtain the value for than
    # place within square
    for row in range(2 * n - 1):
        for col in range(2 * n - 1):
            left = col
            right = 2 * n - 2 - col
            top = row
            bottom = 2 * n - 2 - top
            val = n - min(min(left, right), min(top, bottom))
            print(val, end="")
        print()
    pass
