"""
https://www.naukri.com/code360/problems/alpha-ramp_6581888?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
Alpha-Ramp
A
B B
C C C
D D D D
"""


def alphaRamp(n: int) -> None:
    val = 65
    for i in range(n):
        for j in range(i+1):
            print(chr(val), end=" ")
        print()
        val += 1
    """# different approach
    for i in range(1, n+1):
        val = chr(64 +i)
        print((val+" ")*i)
    """
    pass


val: int = int(input())

alphaRamp(val)

