"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
Given two strings s and p, return an array of all the start indices of p's
anagrams
 in s. You may return the answer in any order.
"""

from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        # declaring variables
        lp, ls = len(p), len(s)
        p_count = Counter(p)
        window_count = Counter(s[:lp]) # intial window count
        # check if inital window count matches the p_count
        if window_count == p_count:
            res.append(0)

        for i in range(lp,ls):
            #update the window_count
            window_count[s[i]] +=1
            window_count[s[i-lp]] -=1

            # remove elements that are zero
            if window_count[s[i - lp]] == 0:
                del window_count[s[i - lp]]

            # Compare with p_count
            if window_count == p_count:
                res.append(i - lp + 1)
        return res


sol = Solution()

print(sol.findAnagrams("cbaebabacd", "abc"))