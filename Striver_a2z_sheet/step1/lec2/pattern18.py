'''
https://www.naukri.com/code360/problems/alpha-triangle_6581429?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SUBMISSION
Alpha Triangle
C
C B
C B A
'''


def alphaTriangle(n: int):
    for row in range(1 , n +1):
        char = 64 + n
        for col in range(row):
            print(chr(char), end=" ")
            char -= 1
        print()
    pass


num = int(input())
alphaTriangle(num)