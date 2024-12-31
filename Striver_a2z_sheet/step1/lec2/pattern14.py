"""
https://www.naukri.com/code360/problems/increasing-letter-triangle_6581897?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SUBMISSION
 Increasing Letter Triangle
A
A B
A B C
"""

def nLetterTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(1, n+1):
        val = 'A'
        for j in range(1,i+1):
            print(val, end =" ")
            val = chr(ord(val) + 1)
        print()


val: int = int(input())

nLetterTriangle(val)