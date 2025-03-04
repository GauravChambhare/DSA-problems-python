class Solution:
    """
    def lcmAndGcd(a: int, b: int) -> list[int]:
        # code here
        # gcd
        l = [0, 0]
        gcd = 1
        for x in range(min(a, b)+1, 0, -1):
            if a % x == 0 and b % x == 0:
                gcd = x
                break
        lcm = int((a * b) / gcd)
        l[0], l[1] = lcm, gcd
        return l
    """

    # Another method using euclidian theorem
    def gcd(self, a: int, b: int) -> int:
        while a > 0 and b > 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        if a == 0:
            return b
        else:
            return a

    def lcmAndGcd(self, a: int, b: int) -> list[int]:

        ans = [0, 0]
        ans[1] = self.gcd(a, b)
        ans[0] = (a * b) // ans[1]

        return ans


n = int(input())
m = int(input())
sol = Solution()
print(sol.lcmAndGcd(n, m))
