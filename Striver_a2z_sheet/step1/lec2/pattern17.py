"""
https://www.naukri.com/code360/problems/alpha-hill_6581921?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
 Alpha Hill
    A
  A B A
A B C B A
Solution: https://youtu.be/uJA-GVWNjcc?feature=shared&t=1060
"""


def alphaHill(n: int):
    '''
    for row in range(1, n+1):
        # spaces
        for space in range(n-row,0,-1):
            print(" ", end=" ")
        char = 64
        for pat in range(1,2*row):
            if pat > row:
                print(chr(char-1), end=" ")
                char -=1
            else:
                print(chr(char+1), end=" ")
                char +=1
        print()
    pass
    '''
# Another method to solve Alpha hill
    for row in range(n):
        # print space
         for space in range(n-row-1):
             print(' ', end=' ')
         char = 65
         for patt in range(row+1):
             print(chr(char), end=" ")
             char +=1

         char -=2
         for patt in range(row):
            print(chr(char), end=" ")
            char -=1
         print()
    pass



num = int(input())
alphaHill(num)

