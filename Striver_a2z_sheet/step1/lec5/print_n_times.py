"""
https://www.naukri.com/code360/problems/-print-n-times_8380707
Print n times

"""

from typing import *


def printNtimes(n: int) -> List[str]:
    if n == 0:
        return []

    result = printNtimes(n - 1)
    return result + ["Coding Ninjas"]
    pass


n = int(input())
# sol = Solution()
print(printNtimes(n))
