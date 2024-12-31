"""
https://www.naukri.com/code360/problems/star-diamond_6573686?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
problem name - Star Diamond
  *
 ***
*****
*****
 ***
  *
"""

def nStarDiamond(n: int) -> None:
    # Write your code here.
    for i in range(1,n+1):
        for k in range(1,n-i+1):
            print(' ', end="")
        for l in range(1,2*i):
            print('*', end="")
        for k in range(1,n-i+1):
            print(' ', end="")
        print()
    for i in range(1,n+1):
        for k in range(1,i):
            print(' ', end="")
        for l in range(2*(n-i)+1):
            print('*', end="")
        print()


val: int = int(input())

nStarDiamond(val)
