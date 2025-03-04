"""
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/move-all-zeroes-to-end-of-array0751
Move All Zeroes to End

You are given an array arr[] of non-negative integers. Your task is to move all the zeros
in the array to the right end while maintaining the relative order of the non-zero elements.
The operation must be performed in place, meaning you should not use extra space for another array
"""


class Solution:
    def pushZerosToEnd(self, arr):

        l = len(arr)
        nonzeroptr = 0

        for current in range(l):

            if arr[current] != 0:
                arr[nonzeroptr], arr[current] = arr[current], arr[nonzeroptr]
                nonzeroptr += 1

        return arr


val = list(map(int, input("Enter a array: ").split()))
sol = Solution()
print(sol.pushZerosToEnd(val))