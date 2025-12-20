"""

Diagonal
Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

Example

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9)

"""

def get_diagonal(input_tuple):
    diagonal_elements = []
    for i in range(len(input_tuple)):
        diagonal_elements.append(input_tuple[i][i])
    return tuple(diagonal_elements)


input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)