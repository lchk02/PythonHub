""" 279. 完全平方数
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、
4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例1：
输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9

提示：
    1 <= n <= 10^4
"""

from math import sqrt


def num_squares(n):
    dp = [0] * (n + 1)
    for i in range(1, n+1):  # i 表示中间状态的数
        ans = int(1e9)  # 至少需要多少个数
        for j in range(1, int(sqrt(i)) + 1):  # j^2 表示完全平方数
            ans = min(ans, dp[i - j * j])
        dp[i] = ans + 1  # dp[i] = min(dp[i-1] + 1, dp[i-squ] + 1), squ表示完全平方数
    return dp[n]
