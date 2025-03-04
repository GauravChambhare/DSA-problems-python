"""
http://leetcode.com/problems/permutation-in-string/?envType=list&envId=xlep8di5
Given two strings s1 and s2, return true if s2 contains a
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""
from collections import defaultdict
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # first declare variables
        # res: bool = False
        ls1, ls2 = len(s1), len(s2)
        """
        s1_count = defaultdict(int)
        # below is done without using counter
        for val in s1:
            s1_count[val] += 1
        window_count = defaultdict(int)
        for val in s2[:ls1]:
            window_count[val] += 1
        """
        s1_count = Counter(s1)
        window_count = Counter(s2)
        if s1_count == window_count:
            return True

        for i in range(ls1, ls2):
            window_count[s2[i]] += 1
            window_count[s2[i - ls1]] -= 1

            if window_count[s2[i - ls1]] == 0:
                del window_count[s2[i - ls1]]
            if window_count == s1_count:
                return True

        return False


sol = Solution()
print(sol.checkInclusion("ba", "hdaibaiw"))
