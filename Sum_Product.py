"""
Sum and Product
Write a function that calculates the sum and product of all elements in a tuple of numbers.

Example

input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)  # Expected output: 10, 24

"""

def sum_product(input_tuple):
    total_sum = 0
    total_product = 1
    
    for number in input_tuple:
        total_sum += number
        total_product *= number
    
    return total_sum, total_product


input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)