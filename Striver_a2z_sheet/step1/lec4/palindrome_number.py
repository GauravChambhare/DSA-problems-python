"""
https://leetcode.com/problems/palindrome-number/

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x, y = str(x), str(x)[::-1]
        if x == y:
            return True
        return False


sol = Solution()
n = int(input())
print(sol.isPalindrome(n))
