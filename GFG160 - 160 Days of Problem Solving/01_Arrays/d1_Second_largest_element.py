"""
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/second-largest3735
Second Largest

Given an array of positive integers arr[], return the second largest element from the array. If the second largest
element doesn't exist then return -1.
"""


class Solution:
    def getSecondLargest(self, arr):
        
        if len(arr) <2:
            return -1
        
        first = second = float('-inf') 
        
        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second  and num!=first:
                second = num
        
        if second == float('-inf'):
            return -1
        else:
            return second


val = list(map(int, input("Enter a array: ").split()))
sol = Solution()
print(sol.getSecondLargest(val))
