"""
Reverse Key-Value Pairs
Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.

Example:

my_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict(my_dict)

Output:

{1: 'a', 2: 'b', 3: 'c'}

"""

def reverse_dict(my_dict):
    reversed_dict = {}

    for key, value in my_dict.items():
        reversed_dict[value]=key
    return reversed_dict

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))