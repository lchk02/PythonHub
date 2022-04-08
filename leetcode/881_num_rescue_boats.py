""" 881. 救生艇
给定数组people。people[i]表示第 i个人的体重，船的数量不限，每艘船可以承载的最大重量为limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为limit。

返回 承载所有人所需的最小船数。

示例 1：
输入：people = [1,2], limit = 3
输出：1
解释：1 艘船载 (1, 2)

示例 2：
输入：people = [3,2,2,1], limit = 3
输出：3
解释：3 艘船分别载 (1, 2), (2) 和 (3)

示例 3：
输入：people = [3,5,3,4], limit = 5
输出：4
解释：4 艘船分别载 (3), (3), (4), (5)

提示：
    1 <= people.length <= 5 * 10^4
    1 <= people[i] <= limit <= 3 * 10^4
"""

from typing import List


class Solution:
    def num_rescue_boats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j, res = 0, len(people)-1, 0
        while i <= j:
            if people[i] + people[j] > limit:
                j -= 1
            else:
                i += 1
                j -= 1
            res += 1
        return res
