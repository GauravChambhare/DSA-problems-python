"""
https://leetcode.com/problems/maximum-average-subarray-i/description/
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any
answer with a calculation error less than 10-5 will be accepted.
"""

from typing import List


class Solution:
    """
    # Below approach does not work because for all -ve input ans will come out as 0 instead of their actual avg value.

    def findMaxAverage(self, nums: List[int], k: int) -> float:

        nums[n]: List[int]
        k: int

        n = len(nums)
        if n == 1:
            return nums[0]
        lptr, rptr = 0, k
        val = 0
        for lptr in range(n - rptr):
            temp = round(sum(nums[lptr:rptr]) / k, 4)
            if temp > val:
                val = temp
            if rptr == n:
                break
            else:
                rptr += 1
        return val
    """

    # using sliding window approach
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # declare a window
        if len(nums) == 1:
            return float(nums[0])
        windowsum = float(sum(nums[:k]))  # sum of first k elements in the nums
        max_sum = windowsum
        n = len(nums)
        for x in range(k, n):
            windowsum += nums[x] - nums[x - k]
            max_sum = max(windowsum, max_sum)
        return max_sum / k


testcases = [[[1, 12, -5, -6, 50, 3], 4], [[0], 1], [[5, 5, 5, 5, 5], 2], [[-1, -2, -3, -4, -5], 3]]
sol = Solution()
for val in testcases:
    print(
        f"For nums: {val[0]} and k = {val[1]}, max avg of k length contiguous subarray is: {sol.findMaxAverage(val[0], val[1])}")
