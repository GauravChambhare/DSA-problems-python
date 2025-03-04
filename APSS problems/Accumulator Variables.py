# 1. Calculate the Sum of an Array
# Write a function that calculates the sum of all elements in an array by accumulating the total as you iterate.

print('----1--------')


def summ(arr):
    if not arr:
        return 0
    ans = 0
    for val in arr:
        ans += val
    return ans


print(summ([1, 91, 3, 63]))

# 2. Find the Minimum and Maximum Elements
#
# Find the smallest and largest numbers in an array by updating minimum and maximum
# variables during iteration


print('-------2--------')


def calc(arr):
    min, max = 1000000, -10000000

    for val in arr:
        if min > val:
            min = val
        if max < val:
            max = val
    return [min, max]


val = calc([723, 12, 8923, 512])
print('min:', val[0], '---', 'max:', val[1])

# 3. Find the Indices of the Min and Max Elements
# In addition to finding the min and max values, keep track of their positions (indices) in the array.

print('-------3--------')


def calc(arr):
    min, max, minin, maxin = 1000000, -10000000, -1, -1

    for x in range(len(arr)):
        val = arr[x]
        if min > val:
            min, minin = val, x

        if max < val:
            max, maxin = val, x
    return [min, minin, max, maxin]


val = calc([723, 74923, 83, 12, 8923, 512, 938, 18, 933340])
print('min:', val[0], ' index:', val[1], '---', 'max:', val[2], ' index:', val[3])

# 4. Find the Two Smallest/Largest Elements Without Sorting
# Modify your approach to keep track of the two smallest and two largest elements during a
# single pass through the array.
print('-------4--------')


def find_two_smallest_and_largest(arr):
    if len(arr) < 2:
        return "Array must contain at least two elements."

    # Initialize variables to hold the smallest and largest values
    smallest1 = float('inf')
    smallest2 = float('inf')
    largest1 = float('-inf')
    largest2 = float('-inf')

    # Iterate through each number in the array
    for num in arr:
        # Update smallest values
        if num < smallest1:
            smallest2 = smallest1
            smallest1 = num
        elif num < smallest2:
            smallest2 = num

        # Update largest values
        if num > largest1:
            largest2 = largest1
            largest1 = num
        elif num > largest2:
            largest2 = num

    return (smallest1, smallest2), (largest1, largest2)


# Example usage
arr = [10, 4, 3, 5, 8, 12, 7]
smallest, largest = find_two_smallest_and_largest(arr)
print("Two Smallest Elements:", smallest)
print("Two Largest Elements:", largest)

# 5.Count Occurrences of a Specific Element
# Count how many times a given element appears in the array by incrementing a counter whenever
# you encounter it.

print('-------5--------')


def ocurrence(num, arr):
    counter = 0
    for val in arr:
        if val == num:
            counter += 1
    print(counter)
    return counter


# more concise version
def occurrence_f(num, arr):
    counter = arr.count(num)
    print(counter)
    return counter


ocurrence(9, [92, 8, 4, 1, 52, 4, 9, 21])
occurrence_f(9, [92, 8, 4, 1, 52, 4, 9, 21])

# 6.Count Occurrences of All Elements
# Use a dictionary or map to count the number of times each unique element appears
# in the array during a single iteration.


print('-------6--------')


def funct(arr):
    if not arr:
        return {}
    di = dict()
    for val in arr:
        if val in di:
            di[val] += 1
        else:
            di[val] = 1
    print(di)
    ''' both above and below method works
    for val in arr:
        if val in di.keys():
            di[val] += 1
        else:
            di[val] = 1
    print(di)
    '''

    return di


testcase5 = [[6, 8, 19, 32, 8, 4, 1, 10, 83], [], [0, 0, 0, 0, 1, 2]]
for x in testcase5:
    funct(x)

# 7.Find the Two Most Frequent Elements
#
# Find the two elements that appear the most number of times in an array.

print('-------7--------')


def f7(arr):
    if not arr:  # Handle empty input
        print("Array is empty!")
        return None

    # Step 1: Count the frequency of each element
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Step 2: Sort the elements by frequency (highest to lowest)
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    # here lambda x: x[1]  takes x and returns second element within x
    # Step 3: Get the two most frequent elements
    most_frequent = sorted_frequency[0][0]  # The most frequent element
    second_most_frequent = sorted_frequency[1][0] if len(
        sorted_frequency) > 1 else None  # Handle fewer than 2 unique elements

    # Print the results
    print(f"The most frequent element is: {most_frequent}")
    if second_most_frequent is not None:
        print(f"The second most frequent element is: {second_most_frequent}")
    else:
        print("No second most frequent element (only one unique element).")

    return most_frequent, second_most_frequent


# Test the function
testset7 = [6, 8, 19, 32, 8, 4, 1, 10, 83, 8, 6, 6]
f7(testset7)

# 8. Compute Prefix Sums
# Create an array where each element at index i is the sum of all elements up to that index in the original array.
# We call this array prefix sums array.
print('-------8--------')


def f8(arr):
    res = [0] * len(arr)
    '''
    # non optimal approach take O(n*n)
    for i in range(len(arr)):
        res[i] = sum(arr[:i+1])
    print(res)
    return res
    '''
    # optimal O(n) approach
    rsum = 0
    for val in arr:
        rsum += val

    print(res)
    return res


testset81 = [7, 7, 7, 7, 7, 7]
testset82 = [1, 2, 3, 1, 2, 1, 3, 2, 4]
# Expected most frequent: 1, second most frequent: 2 or 3


f8(testset81)

# 9. Find the Sum of Elements in a Given Range

# Given a range (start and end indices), write a function that calculates the sum of elements
# within that range by iterating from the start to the end index and accumulating the sum.
print('-------9--------')


def f9(l, r, arr):
    if not arr:
        print('Empty input array!')
        return 0
    if l < 0 or r >= len(arr) or l > r:
        print('Indices out of bounds!')
        return 0
    result = sum(arr[i] for i in range(l, r + 1))

    print(result)
    return result


testset9 = [[1, 2, []], [2, 4, [0, 0, 0, 0]], [4, 5, [1, 81, 0, 8, 47, 100, 4, 7]], [1, 2, [1, 54, 4]]]

for val in testset9:
    f9(val[0], val[1], val[2])



# 10. Efficient Range Sum Queries Using Prefix Sums
#
# After computing the prefix sums array, answer multiple range sum queries efficiently:
# Instead of summing elements for each query, use the prefix sums array to compute the sum of elements between indices
# i and j in constant time.
# Hint: The sum from index i to j can be calculated as prefix_sum[j] - prefix_sum[i - 1]. This method
# requires understanding how to manipulate indices and handle edge cases when i is 0.
def compute_prefix_sum(arr):
    """Compute the prefix sums array."""
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    return prefix_sum

def range_sum_query(i, j, prefix_sum):
    """Compute the sum of elements from index i to j using the prefix sums array."""
    if i < 0 or j >= len(prefix_sum) or i > j:
        print("Invalid indices!")
        return 0
    if i == 0:
        return prefix_sum[j]
    return prefix_sum[j] - prefix_sum[i - 1]

# Test data
testset10 = [
    [1, 2, []],
    [2, 4, [0, 0, 0, 0]],
    [4, 5, [1, 81, 0, 8, 47, 100, 4, 7]],
    [1, 2, [1, 54, 4]]
]

for val in testset10:
    i, j, arr = val
    if not arr:
        print("Empty input array!")
        continue
    prefix_sum = compute_prefix_sum(arr)
    result = range_sum_query(i, j, prefix_sum)
    print(f"Sum from index {i} to {j}: {result}")
