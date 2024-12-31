"""
https://www.naukri.com/code360/problems/alpha-hill_6581921?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
 Alpha Hill
    A
  A B A
A B C B A
"""


def alphaHill(n: int):
    for i in range(1, n + 1):

        for space in range(2 * (n - i)):
            print(' ', end="")
        val = 65
        for patt in range(2 * i - 1):
            print(chr(val), end=" ")
            if patt > (2 * i - 1) / 2:
                val = val - 1
            else:
                val = val + 1

        for space in range(2 * (n - i)):
            print(' ', end="")
        print()
    pass

    pass


num = int(input())
alphaHill(num)

