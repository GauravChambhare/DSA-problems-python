"""
https://www.geeksforgeeks.org/problems/triangle-number-1661489840/0?ref=gcse_ind
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""


class Solution:

    def printTriangle(self, N):
        for i in range(N, 0, -1):

            for j in range(1,i+1):
                print(j, end=" ")
            print()
        """
        # Another approach can be below
        for i in range(N):
            p = 1

            for j in range(i,N):
                print(p, end=" ")
                p +=1
            print()
        """

sb = Solution()

n: int = int(input())
sb.printTriangle(n)


