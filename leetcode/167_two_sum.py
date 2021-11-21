""" 167. 两数之和 II - 输入有序数组
给定一个已按照 非递减顺序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目
标数 target 。
函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以
答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
 
示例 1：
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

示例 2：
输入：numbers = [2,3,4], target = 6
输出：[1,3]
"""


def two_sum(nums, target):
    n = len(nums)
    i, j = 0, n-1
    while i < j:
        if nums[i] + nums[j] == target:
            return [i+1, j+1]
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            i += 1
    return -1


li = [1, 2]
print(two_sum(li, 4))
