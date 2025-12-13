"""

Duplicate Number
Write a function to remove the duplicate numbers on given integer array/list.

Example

remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]


"""



def remove_duplicates(arr):
    # TODO
    result =[]
    for i in arr:
        if i not in result:
            result.append(i)
        else:
            continue
    return result

remove_duplicates([1, 1, 2, 2, 3, 4, 5])