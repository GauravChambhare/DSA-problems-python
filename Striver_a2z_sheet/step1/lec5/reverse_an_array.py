"""
https://www.geeksforgeeks.org/problems/reverse-an-array/0
Reverse an Array
"""


class Solution():
    """
    def reverseArray(self, arr):
        length = len(arr) - 1
        return self.reverse(arr, 0, length)

    def reverse(self, arr, left, right):
        while left <= right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            return self.reverse(arr, left + 1, right - 1)

        return arr
        """
    """
        # usinf iteration.
        def reverseArray(self, arr):
        
        left, right=0, len(arr)-1
        while left<=right:
            arr[left], arr[right] = arr[right], arr[left]
            left +=1
            right -=1
        return arr
    """


    def reverseArray(self, arr):
        length = len(arr) - 1
        return self.reverse(arr, 0, length)

    def reverse(self, arr, left, right):
        if left >= right:
            return arr

        arr[left], arr[right] = arr[right], arr[left]

        return self.reverse(arr, left + 1, right - 1)


arr = list(map(int, input("Enter array elements: ").split()))
# print(arr)
sol = Solution()
print(sol.reverseArray(arr))
