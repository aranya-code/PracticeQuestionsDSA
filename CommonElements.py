"""

Common Elements
Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

Example

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)

"""

def common_elements(tuple1, tuple2):
    common = set(tuple1).intersection(set(tuple2))
    return common


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = tuple(common_elements(tuple1, tuple2))
print(output_tuple)  # Expected output: (4, 5)