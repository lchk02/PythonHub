""" 剑指 Offer II 004. 只出现一次的数字
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回
那个只出现了一次的元素。

示例 1：
输入：nums = [2,2,3,2]
输出：3

示例 2：
输入：nums = [0,1,0,1,0,1,100]
输出：100

提示：
1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次

进阶：你的算法应该具有线性时间复杂度。你可以不使用额外空间来实现吗？
"""

import collections


def single_number(nums):
    freq = collections.Counter(nums)
    ans = [num for num, occ in freq.items() if occ == 1][0]
    return ans


def single_number1(nums):
    ans = 0
    for i in range(32):
        # 注意此处求出的是补码
        total = sum((n >> i) & 1 for n in nums)
        if total % 3:
            if i == 31:
                # 最高位是1表示这个数是负数，需要根据补码求出原码
                ans -= (1 << i)
            else:
                # 把所有位加起来
                ans |= (1 << i)
    return ans


ls = [-100]
print([bin(i) for i in ls])
print(single_number(ls))
