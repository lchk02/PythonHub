""" 5186. 区间内查询数字的频率
请你设计一个数据结构，它能求出给定子数组内一个给定值的 频率 。
子数组中一个值的 频率 指的是这个子数组中这个值的出现次数。

请你实现 RangeFreqQuery 类：
RangeFreqQuery(int[] arr) 用下标从 0 开始的整数数组 arr 构造一个类的实例。
int query(int left, int right, int value) 返回子数组 arr[left...right] 中 value 的
频率 。
一个 子数组 指的是数组中一段连续的元素。arr[left...right] 指的是 nums 中包含下标 left 和
right 在内 的中间一段连续元素。

示例 1：
输入：
["RangeFreqQuery", "query", "query"]
[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
输出：22:[4, 8]  2, 5
[null, 1, 2]
解释：
RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34,
33, 22, 12, 34, 56]);
rangeFreqQuery.query(1, 2, 4); // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。
rangeFreqQuery.query(0, 11, 33); // 返回 2 。33 在整个子数组中出现 2 次。
"""
import bisect
from collections import defaultdict


class RangeFreqQuery:

    def __init__(self, arr):
        self.rf = defaultdict(list)
        for idx, val in enumerate(arr):
            self.rf[val].append(idx)

    def query(self, left, right, value):
        temp = self.rf[value]
        return bisect.bisect_right(temp, right) - bisect.bisect_left(temp, left)


obj = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
param = obj.query(0, 11, 33)
print(param)