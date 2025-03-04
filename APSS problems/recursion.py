from functools import lru_cache

# 1. Calculate the nth Fibonacci Number
# Write a recursive function to find the nth Fibonacci number, where each number
# is the sum of the two preceding ones.

print('--------1--------')


@lru_cache(maxsize=100)
def f1(n):
    if n < 2:
        return n
    return f1(n - 1) + f1(n - 2)


testset1 = [3, 0, 100, 2, 73, 5, 1]

for val in testset1:
    print(f1(val))

# 2.Sum of an Array Using Recursion
# Find the sum of all elements in an array by recursively summing the first element and the sum of
# the rest of the array.

print('--------2--------')


def recursive_sum(arr, index=0):
    # Base case: When the index reaches the length of the array
    if index == len(arr):
        return 0
    # Recursive case: Add the current element to the sum of the rest
    return arr[index] + recursive_sum(arr, index + 1)


test_cases = [
    [[], 0],  # Empty array
    [[1], 1],  # Single-element array
    [[1, 2, 3], 3],  # Small array
    [[0, 0, 0, 0], 4],  # Array of zeros
    [[-1, -2, -3], 4],  # Array with negative numbers
    [[10, 20, 30], 3],  # Positive numbers
    [[1, -1, 1, -1], 4],  # Mixed positive and negative numbers
    [[100], 1],  # Single large number
    [[5, 15, 25, 35], 4],  # Array with a step of 10
    [[1] * 100, 100]  # Large array with repetitive elements
]

# Running the test cases
for test in test_cases:
    arr, expected = test
    result = recursive_sum(arr)
    print(f"Array: {arr}, Sum is : {result}")

print(recursive_sum([1, 2, 3, 4, 5], 5))

# 3. Find the Minimum Element in an Array Using Recursion
#
# Find the smallest element in an array without using loops by comparing the first element with the minimum of the rest of the array.

print('--------3--------')


def f3(arr, n=0):
    if not arr:
        return None
    if n == len(arr) - 1:
        return arr[n]

    return min(arr[n], f3(arr, n + 1))


testcases3 = [[], [0, 0], [3, 51, 9, 7], [-1, 9, 42, -23], [5, 3]]

for val in testcases3:
    print(f3(val))

# 4. Reverse a String Using Recursion
#
# Reverse a given string by recursively swapping characters from the ends towards the center.


print('--------4--------')


def reverse_string_recursive_no_slicing(inputstr, start, end, result=None):
    if result is None:
        result = list(inputstr)  # Convert string to list for mutability

    # Base case: When start index meets or crosses end index
    if start >= end:
        return ''.join(result)

    # Swap characters at start and end
    result[start], result[end] = result[end], result[start]

    # Recursive step: Move towards the middle
    return reverse_string_recursive_no_slicing(inputstr, start + 1, end - 1, result)


# Test cases
testcase4 = [
    ['', ''],  # Empty string
    ['abc', 'cba'],  # Odd-length string
    ['abcdef', 'fedcba'],  # Even-length string
    ['a!b@c#d$', '$d#c@b!a'],  # String with special characters
    ['madam', 'madam'],  # Palindrome
    ['123456789', '987654321'],  # Numbers
    [' space ', ' ecaps ']  # String with spaces
]

for val in testcase4:
    input_str, expected = val
    result = reverse_string_recursive_no_slicing(input_str, 0, len(input_str) - 1)
    print(
        f"Input: {input_str} | Reversed: {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")

print('--------4B--------')


#  another method to solve the problem

def reverse_string_recursive(inputstr):
    # Base case: If the string is empty or has only one character
    if len(inputstr) <= 1:
        return inputstr

    # Recursive case: Reverse the rest of the string and add the current first character to the end
    return inputstr[-1] + reverse_string_recursive(inputstr[:-1])


# Test cases
testcase4 = [
    ['', ''],  # Empty string
    ['abc', 'cba'],  # Odd-length string
    ['abcdef', 'fedcba'],  # Even-length string
    ['a!b@c#d$', '$d#c@b!a'],  # String with special characters
    ['madam', 'madam'],  # Palindrome
    ['123456789', '987654321'],  # Numbers
    [' space ', ' ecaps ']  # String with spaces
]

for val in testcase4:
    input_str, expected = val
    result = reverse_string_recursive(input_str)
    print(
        f"Input: {input_str} | Reversed: {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")

# 5. Check if a String is a Palindrome Using Recursion
# Determine if a string reads the same backward as forward by comparing characters from the outside in.

print('--------5--------')


def f5(ip, left, right, result=None):
    if not result:
        result = list(ip)

    if left >= right:
        return True
    if result[left] != result[right]:
        return False
    else:
        return f5(str, left + 1, right - 1, result)


testcase5 = ['abc', 'madam', 'hellokitty', '$fi*2(k!']

for val in testcase5:
    res = f5(val, 0, len(val) - 1)
    print(f"Input {val} is,{'palindrome' if res == True else 'Not a palindrome'}")


# 6. Generate All Permutations of a String
# Recursively generate all permutations of the characters in a string by swapping characters.
