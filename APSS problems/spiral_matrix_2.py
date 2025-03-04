"""
https://leetcode.com/problems/spiral-matrix-ii/description/
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
"""


def spiral_matrix(n: int):
    frame = [[0 for _ in range(n)] for _ in range(n)]
    # print(frame)

    top, bottom, left, right = 0, n-1, 0, n-1
    index = 1

    while index <= n**2:

        # traverse top row from left to right
        for j in range(left, right+1):
            frame[top][j] = index
            index += 1
        top += 1
        # traverse right col from top to bottom
        for i in range(top, bottom+1):
            frame[i][right] = index
            index += 1
        right -= 1
        # traverse bottom row from right to left
        for j in range(right, left-1, -1):
            frame[bottom][j] = index
            index += 1
        bottom -=1
        # traverse left col from bottom to top
        for i in range(bottom, top -1, -1):
            frame[i][left] = index
            index += 1
        left += 1

    return frame


n = int(input("Enter an integer :"))
res = spiral_matrix(n)
for row in res:
    print(row)

