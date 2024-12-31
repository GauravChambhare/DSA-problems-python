"""
*
* *
* * *
 https://www.geeksforgeeks.org/problems/right-triangle/0?ref=gcse_ind
"""
class Solution:
    def printTriangle(self, N):

        for i in range(0, N):

            for j in range(i+1):

                print('* ', end='')
            print()


num: int = int(input())

sb = Solution()
sb.printTriangle(num)

