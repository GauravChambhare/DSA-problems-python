"""
https://leetcode.com/problems/valid-palindrome/description/
Valid Palindrome
"""

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        rp: int = len(s) - 1
        lp: int = 0
        s = s.lower()
        regex: str = "[^a-zA-Z0-9]"
        s = re.sub(regex, "", s)
        return self.checker(s, lp, rp)

    def checker(self, s, lp, rp):
        if lp >= rp:
            return True
        if s[lp] != s[rp]:
            return False
        return self.checker(s, lp + 1, rp - 1)  # Use self here

"""
    # Easier approach
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""

        for c in s:
            if c.isalnum():
                newstr += c.lower()
        return newstr == newstr[::-1]
"""
n = str(input())
sol = Solution()
print(sol.isPalindrome(n))
