"""
https://naukri.com/code360/problems/reverse-letter-triangle_6581906?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
Reverse Letter Triangle
A B C
A B
A
"""


def nLetterTriangle(n: int):
    # Write your solution here.

    for i in range(n):
        val='A'
        for j in range(n-i, 0, -1):
            print(val, end=" ")
            val = chr(ord(val)+1)
        print()
    pass


val: int = int(input())

nLetterTriangle(val)

