'''
https://www.naukri.com/code360/problems/symmetric-void_6581919?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=PROBLEM
Symmetric void
* * * * * *
* *     * *
*         *
*         *
* *     * *
* * * * * *

'''


def symmetry(n: int):

    for i in range(n):

        # print *

        for y in range(n-i):

            print("*",end=' ')

        # print gap

        for o in range(2*i):

            print(" ",end=' ')

        # reverse *

        for j in range(n-i):

            print("*",end=' ')

        # newline

        print()

    for s in range(n):

        # print *

        for y in range(s+1):

            print("*",end=' ')

        # print gap

        gap = 2*(n-1)

        for o in range(gap-(2*s)):

            print(" ",end=' ')

        # reverse *

        for j in range(s+1):

            print("*",end=' ')

        print()

    pass

num = int(input())
symmetry(num)