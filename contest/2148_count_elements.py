""" 2148. 元素计数（277周赛，1）
给你一个整数数组 nums ，统计并返回在 nums 中同时至少具有一个严格较小元素和一个严格较大元素的元素数目。

示例 1：
输入：nums = [11,7,2,15]
输出：2
解释：元素 7 ：严格较小元素是元素 2 ，严格较大元素是元素 11 。
元素 11 ：严格较小元素是元素 7 ，严格较大元素是元素 15 。
总计有 2 个元素都满足在 nums 中同时存在一个严格较小元素和一个严格较大元素。

示例 2：
输入：nums = [-3,3,3,90]
输出：2
解释：元素 3 ：严格较小元素是元素 -3 ，严格较大元素是元素 90 。
由于有两个元素的值为 3 ，总计有 2 个元素都满足在 nums 中同时存在一个严格较小元素和一个严格较大元素。

提示：
    1 <= nums.length <= 100
    -10^5 <= nums[i] <= 10^5
"""

from bisect import bisect_left, bisect_right


def count_elements(nums):
    nums.sort()
    ans = 0
    if nums[0] != nums[-1]:
        ans = bisect_left(nums, nums[-1]) - bisect_right(nums, nums[0])
    return ans
