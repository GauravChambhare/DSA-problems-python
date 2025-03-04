"""
https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1
Sum 1 to n Divisors
"""

class Solution:

    def sumOfDivisors(self, n):
        #code here
        sum=0
        for x in range(1,n+1):
            sum = sum + x*(n//x)
        return sum



n = int(input())
sol = Solution()
print(sol.sumOfDivisors(n))
