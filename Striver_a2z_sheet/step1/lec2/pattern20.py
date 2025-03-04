'''
https://www.naukri.com/code360/problems/symmetry_6581914?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
Symmetry
*         *
* *     * *
* * * * * *
* *     * *
*         *
'''


def symmetry(n: int):
    for row in range(n):
        for pat in range(row+1):
            print("*", end=" ")
        for space in range(2*(n-row-1)):
            print(" ", end=" ")
        for pat in range(row+1):
            print("*", end=" ")
        print()
    for row in range(n-1):
        for pat in range(n-row-1):
            print("*", end=" ")
        for space in range(2*(row+1)):
            print(" ", end=" ")
        for pat in range(n-row-1):
            print("*", end=" ")
        print()
    pass


n = int(input())
symmetry(n)