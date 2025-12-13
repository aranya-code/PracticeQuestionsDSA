"""
Max Product of Two Integers
Find the maximum product of two integers in an array where all elements are positive.

Example

arr = [1, 7, 3, 4, 9, 5] 
max_product(arr) # Output: 63 (9*7)

"""
arr = [1, 7, 3, 4, 9, 5]

def max_product(arr):
    # TODO
    arr.sort()
    return arr[-2] * arr[-1]


max_product(arr)
        
