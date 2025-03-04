from typing import List

# 3 .
# Write a function that accesses every other element in the array, starting from the first element.
print("-------3--------")


def fetch(arr):
    res = []
    for i in range(len(arr)):
        if i % 2 != 0:
            res.append(arr[i])
    return res


print(fetch([1, 2, 3, 4, 5, 6, 7, 8]))

# 4. Find the Index of a Target Element
# Write a function that searches for a specific element in an array and returns its index. If the
# element is not found, return -1.
print("-------4--------")


def find(n: int, arr: list[int]) -> int:
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1


print(find(5, [9, 10, 73, 671, 1, 6, 5, 721]))

# 5.
# Find the First Prime Number in an Array
# Iterate over an array and find the first prime number. Stop the iteration once you find it.

print("-------5--------")


def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is the only even prime number
    if num % 2 == 0:
        return False  # Exclude all other even numbers
    for i in range(3, int(num ** 0.5) + 1, 2):  # Check only odd divisors
        if num % i == 0:
            return False
    return True


def first_prime_no(arr: list[int]) -> int:
    """Find the first prime number in an array."""
    return next((x for x in arr if is_prime(x)), -1)


# Test the function
print(first_prime_no([4, 90, 5, 721, 82]))  # Output: 5

# 6. Traverse a Two-Dimensional Array
#
# Write a function to print all elements of a 2D array (matrix), row by row.

print("-------6--------")


def array_traversal(arr):
    res = []
    for item in arr:
        for subitem in item:
            res.append(subitem)
    '''this can also be done using list comprehension'''

    return res


def flatten_2d_array(arr):
    res = [subitem for item in arr for subitem in item]
    return res


inp = [[1, 2], [3, 4], [5, 6, 7]]
print(f'For input of array {inp} - ', array_traversal(inp))
print(f'For input of array {inp} using flattening - ', flatten_2d_array(inp))

#  7.Traverse the Main Diagonal of a Matrix

# Print the elements along the main diagonal of a square matrix, where the row and column
# indices are equal.
print("-------7--------")


# a square matirx will be nxn


def main_diag(arr):
    res = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                res.append(arr[i][j])

    return res


def comprehension(arr):
    res = [arr[i][j] for i in range(len(arr)) for j in range(len(arr[i])) if i == j]
    return res


val = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'For square matrix {val} - ', main_diag(val))
print(f'For square matrix {val} using list comprehension - ', comprehension(val))

#  8.Traverse the Perimeter of a Matrix
#
# Print the elements along the outer edge (perimeter) of a 2D array.

print("-------8--------")

for row in val:
    print(row)


def traverse_perimeter(arr):
    left, right, top, bottom = 0, len(arr[0]) - 1, 0, len(arr) - 1
    res = []
    # for row in range(len(arr)):
    #     for col in range(len(arr[row])):
    #         if min(min(left, right), min(top, bottom)) == 0:
    #             res.append(arr[row][col])
    #         left += 1
    #         right -= 1
    #     top +=1
    #     bottom -=1
    #     left = 0
    #     right = len(arr[0]) - 1
    # x = 1
    # while(x > 0):

    # left -> right
    left, right = 0, len(arr[0]) - 1
    top, bottom = 0, len(arr) - 1
    res = []

    # Traverse from left to right along the top row
    for col in range(left, right + 1):
        res.append(arr[top][col])

    # Traverse from top to bottom along the right column
    for row in range(top + 1, bottom + 1):
        res.append(arr[row][right])

    # Traverse from right to left along the bottom row if there's more than one row
    if bottom > top:
        for col in range(right - 1, left - 1, -1):
            res.append(arr[bottom][col])

    # Traverse from bottom to top along the left column if there's more than one column
    if left < right:
        for row in range(bottom - 1, top, -1):
            res.append(arr[row][left])

    return res


print(f'Traversal order of 2d matrix {val} is - ', traverse_perimeter(val))

# 9. Traverse Elements in Spiral Order
# Print elements of a 2D array in spiral order, starting from the top-left corner and moving inward.
#

print("-------9--------")


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
        print(top, '--', bottom)
        for row in range(top, bottom + 1):
            print('top -> down')
            ans.append(matrix[row][right])
        right -= 1
        if top < bottom:
            for col in range(right, left - 1, -1):
                ans.append(matrix[bottom][col])
            bottom -= 1
        if left < right:
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

input = [[1, 2, 3]]
print(spiralOrder(input))



# 10. Traverse the Lower Triangle of a Matrix
# Print the elements below and including the main diagonal of a square matrix.

print("-------10--------")
# main diagonal + lower elements
def main_diag(arr):
    res = []

    for i in range(len(arr[0])):
        for j in range(len(arr)):
            if i >= j:
                print(arr[i][j], end=" ")
                res.append(arr[i][j])
        print()
    return res

'''
1  2  3
4  5  6
7  8  9
'''


def lower_triangle(arr):

    val =  main_diag(arr)
    return val

input = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# input = [[1, 2, 3]]
print(lower_triangle(input))
