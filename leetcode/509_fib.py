""" 509. 斐波那契数
斐波那契数（通常用F(n) 表示）形成的序列称为 斐波那契数列 。该数列由0 和 1 开始，后面的每一项数
字都是前面两项数字的和。也就是：

F(0) = 0，F(1)= 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定n ，请计算 F(n) 。

示例 1：
输入：n = 2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1

示例 2：
输入：n = 3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2

示例 3：
输入：n = 4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3

提示：
    0 <= n <= 30
"""


class Solution:
    def fib(self, n: int) -> int:
        """
        动态规划
        :param n:
        :return:
        """
        if n < 2:
            return n
        else:
            p, q = 0, 1
            for i in range(2, n+1):
                p, q = q, p + q
            return q

    def fib2(self, n: int) -> int:
        """
        递归
        :param n:
        :return:
        """
        if n < 2:
            return n
        else:
            return self.fib2(n-1) + self.fib2(n-2)
