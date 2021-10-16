#!/usr/bin/python3

""" 26. 删除有序数组中的重复项
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后
数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1：
输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数
组中超出新长度后面的元素。
"""

num1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def remove_duplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            nums[i + 1] = nums[j]
            i += 1
    return i + 1


print(remove_duplicates(num1))