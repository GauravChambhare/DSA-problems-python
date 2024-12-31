"""
https://www.geeksforgeeks.org/problems/triangle-pattern/1
* * *
* *
*
"""
"""
class Solution:
    def printTriangle(self, N):

        for i in range(N,0,-1):
            print("* "*i)
"""
# different method

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(N - i):
                print("*", end=" ")
            print()


N: int = int(input())
sb = Solution()
sb.printTriangle(N)



