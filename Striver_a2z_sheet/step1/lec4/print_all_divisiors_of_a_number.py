"""
https://www.naukri.com/code360/problems/print-all-divisors-of-a-number_1164188?leftPanelTabValue=PROBLEM
Print all Divisors of a number
"""


from typing import List


def printDivisors(n: int) -> List[int]:
    divisors = []

    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            divisors.append(x)
            if x != n // x:
                divisors.append(n // x)

    return sorted(divisors)
    pass


n = int(input())
print(printDivisors(n))

