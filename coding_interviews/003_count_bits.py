""" 剑指 Offer II 003. 前 n 个数字二进制中 1 的个数
给定一个非负整数 n ，请计算 0 到 n 之间的每个数字的二进制表示中 1 的个数，并输出一个数组。

示例 1:
输入: n = 2
输出: [0,1,1]
解释:
0 --> 0
1 --> 1
2 --> 10

示例 2:
输入: n = 5
输出: [0,1,1,2,1,2]
解释:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

说明 :
    0 <= n <= 10^5

进阶:
给出时间复杂度为 O(n*sizeof(integer)) 的解答非常容易。但你可以在线性时间 O(n) 内用一趟扫描
做到吗？
要求算法的空间复杂度为 O(n) 。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的
__builtin_popcount ）来执行此操作。
"""


def count_bits(n):
    return [bin(i).count("1") for i in range(n+1)]


def count_bits2(n):
    result = [i for i in range(n+1)]
    for i in range(1, n+1):
        result[i] = result[i & (i-1)] + 1
    return result
