""" 221. 最大正方形
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],
["1","0","0","1","0"]]
输出：4

示例 2：
输入：matrix = [["0","1"],["1","0"]]
输出：1

示例 3：
输入：matrix = [["0"]]
输出：0

提示：
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 300
    matrix[i][j] 为 '0' 或 '1'
"""


def maximal_square(matrix):
    m, n = len(matrix), len(matrix[0])
    dp, max_side = [[0] * n for _ in range(m)], 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                dp[i][j] = 1 if i == 0 or j == 0 else min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    return max_side * max_side
