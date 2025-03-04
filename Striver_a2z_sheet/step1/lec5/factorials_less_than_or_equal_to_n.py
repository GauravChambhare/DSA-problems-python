"""
https://www.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/0?problemType=functional&difficulty%255B%255D=-1&page=1&query=problemTypefunctionaldifficulty%255B%255D-1page1
Factorials Less than or Equal to n

"""


class Solution:
    def factorials(self, n) -> int:
        if n == 1:
            return 1
        return n * self.factorials(n - 1)

    def factorialNumbers(self, n):
        # code here
        vals = []
        for x in range(1, n + 1):
            if self.factorials(x) <= n:
                vals.append(self.factorials(x))
        return vals


"""
# without using recursion

from typing import List
class Solution:
    def factorialNumbers(self, n) -> List[int]:
    # 	 declaring variables for empty list, a counter and fact value
        result: List[int] =[]
        fact: int = 1
        counter: int = 1
        
        while fact <=n:
            result.append(fact)
            counter +=1
            fact *= counter
            
        return result

"""


n = int(input())
sol = Solution()
print(sol.factorialNumbers(n))
