""" 217. 存在重复元素
给定一个整数数组，判断是否存在重复元素。
如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false

示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

提示：
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""

from collections import Counter


def contains_duplicate(nums):
    """
    排序
    :param nums:
    :return:
    """
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


def contains_duplicate2(nums):
    """
    哈希表
    :param nums:
    :return:
    """
    cnt = Counter(nums)
    for i in cnt:
        if cnt[i] > 1:
            return True
    return False


def contains_duplicate3(nums):
    """
    集合
    :param nums:
    :return:
    """
    return sum(nums) != sum(set(nums)) if nums.count(0) < 2 else True
