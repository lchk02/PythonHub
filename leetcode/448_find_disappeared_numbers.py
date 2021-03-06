""" 448. 找到所有数组中消失的数字
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范
围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

示例 1：
输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]

示例 2：
输入：nums = [1,1]
输出：[2]

提示：
    n == nums.length
    1 <= n <= 10^5
    1 <= nums[i] <= n

进阶：你能在不使用额外空间且时间复杂度为 O(n) 的情况下解决这个问题吗? 你可以假定返回的数组不算
在额外空间内。
"""

from typing import List


class Solution:
    def find_disappeared_numbers(self, nums: List[int]) -> List[int]:
        res = set([i for i in range(1, len(nums)+1)])
        for n in nums:
            if n in res:
                res.remove(n)
        return list(res)


sl = Solution()
print(sl.find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
