"""
https://www.geeksforgeeks.org/problems/triangle-number/0?ref=gcse_ind
1
1 2
1 2 3
"""

class Solution:
    def printTriangle(self, N):

        for i in range(1, N+ 1):

            for j in range(1, i + 1):
                print(j, end=' ')
            print()


n: int = int(input())

sb = Solution()

sb.printTriangle(n)

