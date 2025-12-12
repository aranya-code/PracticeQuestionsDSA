"""

Array/List Interview Questions

1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


"""

result = []
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                result.append([i, j])
    return result
    
mylist = [2,3,7,11,15,1,9,3]
target = 18
print(two_sum(mylist, target))