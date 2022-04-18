""" 寻找身高相近的小朋友
小明今年升学到了小学1年级
来到新班级后，发现其他小朋友身高参差不齐
然后就想基于各小朋友和自己的身高差，对他们进行排序
请帮他实现排序
输入描述
第一行为正整数 h和n
0<h<200 为小明的身高
0<n<50 为新班级其他小朋友个数
第二行为n各正整数
h1 ~ hn分别是其他小朋友的身高
取值范围0<hi<200
且n个正整数各不相同

输出描述
输出排序结果，各正整数以空格分割
和小明身高差绝对值最小的小朋友排在前面
和小明身高差绝对值最大的小朋友排在后面
如果两个小朋友和小明身高差一样
则个子较小的小朋友排在前面

示例一
输入
100 10
95 96 97 98 99 101 102 103 104 105
输出
99 101 98 102 97 103 96 104 95 105

说明
小明身高100，班级学生10个，身高分别为95 96 97 98 99 101 102 103 104 105，
按身高差排序后结果为：99 101 98 102 97 103 96 104 95 105。
"""

from typing import List
from collections import defaultdict


class Solution:
    def find_near_hight(self, hm: int, nums: List[int]) -> List[int]:
        distance = defaultdict(list)
        res = []
        for n in nums:
            distance[abs(n - hm)].append(n)
        tmp = []
        for key in distance:
            tmp.append(key)
        tmp.sort()
        for i in tmp:
            distance[i].sort()
            res.extend(distance[i])
        return res


sl = Solution()
print(sl.find_near_hight(100, [95, 96, 97, 98, 99, 101, 102, 103, 104, 105]))
