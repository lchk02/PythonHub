""" 697. 数组的度
给定一个非空且只包含非负数的整数数组nums，数组的 度 的定义是指数组里任一元素出现频数的最大值。

你的任务是在 nums 中找到与nums拥有相同大小的度的最短连续子数组，返回其长度。

示例 1：
输入：nums = [1,2,2,3,1]
输出：2
解释：
输入数组的度是 2 ，因为元素 1 和 2 的出现频数最大，均为 2 。
连续子数组里面拥有相同度的有如下所示：
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组 [2, 2] 的长度为 2 ，所以返回 2 。

示例 2：
输入：nums = [1,2,2,3,1,4,2]
输出：6
解释：
数组的度是 3 ，因为元素 2 重复出现 3 次。
所以 [2,2,3,1,4,2] 是最短子数组，因此返回 6 。

提示：
    nums.length在 1 到 50,000 范围内。
    nums[i]是一个在 0 到 49,999 范围内的整数。
"""

from typing import List
from collections import Counter, defaultdict


class Solution:
    def find_shortest_sub_array(self, nums: List[int]) -> int:
        temp = Counter(nums)
        fre, key = 0, set()
        for k in temp:
            fre = max(temp[k], fre)
        for k in temp:
            if temp[k] == fre:
                key.add(k)
        dt = defaultdict(list)
        for i in range(len(nums)):
            if nums[i] in key:
                dt[nums[i]].append(i)
        res = len(nums)
        for i in dt:
            res = min(dt[i][-1] - dt[i][0] + 1, res)
        return res
