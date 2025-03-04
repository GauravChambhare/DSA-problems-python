"""
https://www.geeksforgeeks.org/problems/print-gfg-n-times/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-gfg-n-times
Print GFG n times
"""


class Solution:
    def printGfg(self, n):
        # Code here
        if n == 0:
            return
        print("GFG", end=" ")
        self.printGfg(n - 1)


n = int(input())
sol = Solution()
sol.printGfg(n)
