'''
https://leetcode.com/problems/spiral-matrix/

'''
from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    # declaring variable
    if not matrix or not matrix[0]:
        return []
    left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    ans = []
    # we will move in clockwise spiral till left col <= right or till top row <= bottom row
    while top <= bottom and left <= right:

        # left to right
        for col in range(left, right + 1):
            ans.append(matrix[top][col])
        top += 1
        # print(top, '--', bottom)
        for row in range(top, bottom + 1):
            # print('top -> down')
            ans.append(matrix[row][right])
            # print(ans[-1])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                ans.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                ans.append(matrix[row][left])
            left += 1
        # for col in range(right, left - 1, -1):
        #     ans.append(matrix[bottom][col])
        # bottom -= 1
        # for row in range(bottom, top - 1, -1):
        #     ans.append(matrix[row][left])
        # left += 1
        # one cycle complete
    return ans


# input = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

input = [[1, 2, 3], [4, 5, 6]]
print(spiralOrder(input))

