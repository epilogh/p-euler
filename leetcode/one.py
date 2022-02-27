"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    listf = []
    for i in range(len(nums)):
        difference = target - nums[i]
        list2 = nums.copy()
        list2 = list2[i+1:]
        if difference in list2:
            position = list2.index(difference)+i+1
            listf = [i, position]
    return(listf)

nums = [2,7,11,15]
target = 9
print(nums, target, twoSum(nums,target))
nums = [3,2,4]
target = 6
print(nums, target, twoSum(nums,target))
nums = [3,3]
target = 6
print(nums, target, twoSum(nums, target))