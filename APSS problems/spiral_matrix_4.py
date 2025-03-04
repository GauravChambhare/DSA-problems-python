# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional, List

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # declare vairables
        left, right, top, bottom = 0, n, 0, m
        # intialize a matrix with mxn
        res = [[-1 for _ in range(n)] for _ in range(m)]
        # return res
        # looping
        while head:
            for col in range(left, right):
                if not head:
                    return res
                res[top][col] = head.val
                head = head.next
            top +=1
            for row in range(top, bottom):
                if not head:
                    return res
                res[row][right-1] = head.val
                head = head.next
            right -=1
            if left <= right:
                for col in range(right-1, left-1, -1):
                    if not head:
                        return res
                    res[bottom-1][col] = head.val
                    head = head.next
                bottom -=1
            if top <= bottom:
                for row in range(bottom -1, top-1,-1):
                    if not head:
                        return res
                    res[row][left] = head.val
                    head = head.next
                left +=1

        return res


m = 3
n = 5
head = [3,0,2,6,8,1,7,9,4,2,5,5,0]