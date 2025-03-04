"""
https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1
Sum of first n terms
"""

class Solution:
    def sumOfSeries(self,n):
        #code here
        if n==1:
            return 1
        return n**3 + self.sumOfSeries(n-1)


sol = Solution()
n = int(input())
print(sol.sumOfSeries(n))