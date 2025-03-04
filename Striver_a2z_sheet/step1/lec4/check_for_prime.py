"""
https://www.naukri.com/code360/problems/check-prime_624934?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
Check Prime
"""


def isPrime(n):
    if n <= 1:
        return "NO"

    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0 and x != 1:
            return "NO"

    return "YES"


n = int(input())
print(isPrime(n))
