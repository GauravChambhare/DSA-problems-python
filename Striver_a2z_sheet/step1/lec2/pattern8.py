"""
https://www.geeksforgeeks.org/problems/triangle-pattern-1661493231/0?ref=gcse_ind
*****
 ***
  *
"""

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i):
                print(' ', end="")
            for k in range(2*(N-i)-1):
                print('*',end="")
            print()
        """
        # Another method is
        for i in range(N):
            print(' ' * i + '*' * (2 * (N - i) - 1))
        """


n: int = int(input())
sb = Solution()
sb.printTriangle(n)
