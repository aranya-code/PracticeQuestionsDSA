"""
Same Frequency
Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

Example:

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)
Output:

False

"""

def check_same_frequency(list1, list2):

    if len(list1) != len(list2):
        return False
    
    frequency1 = {}
    frequency2 = {}

    for item in list1:
        frequency1[item] = frequency1.get(item, 0) +1
    
    for item in list2:
        frequency2[item] = frequency2.get(item, 0) +1
    
    return frequency1 == frequency2