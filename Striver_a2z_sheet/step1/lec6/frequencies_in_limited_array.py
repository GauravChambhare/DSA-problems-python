"""
Frequencies in a Limited Array


You are given an array arr[] containing positive integers. The elements in the array arr[] range
from 1 to n (where n is the size of the array), and some numbers may be repeated or absent. Your
task is to count the frequency of all numbers in the range 1 to n and return an array of size n
such that result[i] represents the frequency of the number i (1-based indexing).
"""


# Method one

class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def hashtable(self, val: int, arr):

        self.MAX = val
        self.res = [0] * val

        index = 0
        for i in range(0, self.MAX):
            if arr[i] > N or arr[i] < 1:
                continue
            else:
                index = arr[i] - 1
            self.res[index] += 1

        return self.res

    def frequencyCount(self, arr):
        #  code here
        return self.hashtable(len(arr), arr)

# Method 2

    def frequencyCount1(self, arr):
        r = []
        for i in range(1, len(arr) + 1):
            r1 = arr.count(i)
            r.append(r1)
        return r

    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount2(self, arr):
        l = [0 for i in range(len(arr))]
        for i in arr:
            l[i-1]+=1
        return l


# val = list(map(int, input("Enter a array: ").split()))
val = [2, 3, 2, 3, 5]
sol = Solution()
print(sol.frequencyCount(val))
print(sol.frequencyCount1(val))
print(sol.frequencyCount2(val))


# 2 3 2 3 5
