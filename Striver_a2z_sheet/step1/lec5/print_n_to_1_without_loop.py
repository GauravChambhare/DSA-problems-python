"""
https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/0?ref=gcse_ind
Print N to 1 without loop

"""


class Solution:
    def printNos(self, n):
        # Code here
        if n==0:
            return
        print(n, end=" ")
        self.printNos(n-1)


sol = Solution()
n = int(input())
sol.printNos(n)
