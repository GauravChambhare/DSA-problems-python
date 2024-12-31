"""
https://www.geeksforgeeks.org/problems/triangle-number-1661428795/1

"""


class Solution:
    def printTriangle(self, N):

        for i in range(1, N+1):

            for j in range(1, i + 1):
                print(i, end= ' ')
            print()


n: int = int(input())
sb = Solution()
sb.printTriangle(n)
