"""
1
2 2
3 3 3 
problem link - https://www.geeksforgeeks.org/problems/square-pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_1
"""


class Solution:
    def printSquare(self, N):
        # Code here
        for _ in range(0, N):
            for _ in range(0, N):
                print('* ', end='')

            print()


num: int = int(input("Enter a positive integer"))

sb = Solution()  # creating an object of solution class to access the printSquare function.
sb.printSquare(num)
