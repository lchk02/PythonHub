""" 977. 有序数组的平方
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求
也按 非递减顺序 排序。

示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]

示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]

提示：
    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums 已按 非递减顺序 排序

进阶：
    请你设计时间复杂度为 O(n) 的算法解决本问题
"""

from random import randint
from copy import deepcopy

from algorithm.quick_sort import quick_sort
from algorithm.cal_time import cal_time


@cal_time
def sorted_squares(nums):
    for i in range(0, len(nums)):
        nums[i] = nums[i] ** 2
    return quick_sort(nums)


@cal_time
def sorted_squares2(nums):
    n = len(nums)
    i, j = 0, n-1
    while i <= j:
        mid = (j - i) // 2 + i
        if nums[mid] < 0:
            i = mid + 1
        else:
            j = mid - 1
    i, j = i-1, i
    ans = list()
    while i >= 0 or j < n:
        if i < 0:
            ans.append(nums[j] * nums[j])
            j += 1
        elif j == n:
            ans.append(nums[i] * nums[i])
            i -= 1
        elif nums[i] * nums[i] < nums[j] * nums[j]:
            ans.append(nums[i] * nums[i])
            i -= 1
        else:
            ans.append(nums[j] * nums[j])
            j += 1
    return ans


@cal_time
def sorted_squares3(nums):
    n = len(nums)
    ans = [0] * n
    i, j = 0, n-1
    while i <= j:
        i2 = nums[i] ** 2
        j2 = nums[j] ** 2
        if i2 > j2:
            ans[n-1] = i2
            i += 1
        else:
            ans[n-1] = j2
            j -= 1
        n -= 1
    return ans


li = sorted([randint(-9999, 9999) for i in range(10000)])
li2 = deepcopy(li)
print("原始数组：", li)
print(sorted_squares2(li))
print(sorted_squares3(li2))
