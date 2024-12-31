"""
https://www.geeksforgeeks.org/problems/triangle-pattern-1661492263/0?ref=gcse_ind
  *
 ***
*****
"""


class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(N-i-1):
                print(' ', end='')
            for k in range(2*i+1):
                print('*', end='')

            print()


n: int = int(input())
sb = Solution()
sb.printTriangle(n)