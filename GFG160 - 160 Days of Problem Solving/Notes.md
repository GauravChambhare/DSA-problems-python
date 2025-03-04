[GfG 160 - 160 Days of Problem Solving](https://www.geeksforgeeks.org/batch/gfg-160-problems?tab=Chapters)
---


*Second Largest Element in an Array- GFG160 - 160 Days of Problem Solving/01_Arrays/d1_Second_largest_element.py*


**Problem Statement**:  
Given an array of positive integers `arr[]`, return the second largest element. If it doesn't exist, return -1.

#### Solution Method

1. Initialize `first` and `second` to negative infinity.
2. Iterate through the array:
   - Update `first` and `second` based on the current number.
3. Return `second` if it was updated; otherwise, return -1.

#### Code Implementation

```python
class Solution:
    def getSecondLargest(self, arr):
        first = second = float('-inf')
        for num in arr:
            if num > first: second, first = first, num
            elif num > second and num != first: second = num
        return second if second != float('-inf') else -1

val = list(map(int, input("Enter an array: ").split()))
sol = Solution()
print(sol.getSecondLargest(val))
```

This method efficiently finds the second largest element in a single pass through the array.


===========================
---
*Move All Zeroes to End - GFG160 - 160 Days of Problem Solving/01_Arrays/d2_move_all_zeroes_to_end.py*

```python
class Solution:
	def pushZerosToEnd(self,arr):

        l= len(arr)
        nonzeroptr = 0
        
        for current in range(l):
            
            if arr[current]!=0:
                
                arr[nonzeroptr], arr[current] = arr[current], arr[nonzeroptr]
                nonzeroptr += 1
                
        return arr
```

Here’s the efficient solution using the **two-pointer technique**:

```python
class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        nonZeroPointer = 0  # Tracks where the next non-zero element should go

        # Traverse the array
        for current in range(n):
            if arr[current] != 0:
                # Swap non-zero element with the position at nonZeroPointer
                arr[nonZeroPointer], arr[current] = arr[current], arr[nonZeroPointer]
                nonZeroPointer += 1

        return arr
```

### Explanation of the Code:
1. **Initialization**:
   - `nonZeroPointer` starts at index `0`, the position where the next non-zero element should be placed.

2. **Traversal**:
   - Iterate over the array with `current`.
   - If the current element is non-zero, swap it with the element at `nonZeroPointer`.
   - Increment `nonZeroPointer` to the next index.

3. **Efficiency**:
   - This approach ensures all non-zero elements are placed at the beginning in their original order.
   - Zeros are automatically shifted to the end because of the swapping.
   - The algorithm runs in **O(n)** time with **O(1)** space.

### Example:
For `arr = [1, 0, 2, 3, 0, 4, 0]`:
1. After processing `1`: `[1, 0, 2, 3, 0, 4, 0]` (`nonZeroPointer = 1`)
2. After processing `2`: `[1, 2, 0, 3, 0, 4, 0]` (`nonZeroPointer = 2`)
3. After processing `3`: `[1, 2, 3, 0, 0, 4, 0]` (`nonZeroPointer = 3`)
4. After processing `4`: `[1, 2, 3, 4, 0, 0, 0]` (`nonZeroPointer = 4`)

Final output: `[1, 2, 3, 4, 0, 0, 0]`



===========================
---