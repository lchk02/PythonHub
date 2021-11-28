""" 剑指 Offer II 002. 二进制加法
给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。
输入为 非空 字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "10"
输出: "101"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
"""


def add_binary(a, b):
    flag = 0
    result = []
    i, j = len(a) - 1, len(b) - 1
    while i > -1 or j > -1:
        tmp_a = int(a[i]) if i > -1 else 0
        tmp_b = int(b[j]) if j > -1 else 0
        i -= 1
        j -= 1
        tmp_sum = tmp_a + tmp_b + flag
        flag = 0 if tmp_sum < 2 else 1
        tmp_sum = tmp_sum if tmp_sum < 2 else tmp_sum - 2
        result.append(str(tmp_sum))
    if flag:
        result.append('1')
    result.reverse()
    return ''.join(result)


def add_binary2(a, b):
    x, y = int(a, 2), int(b, 2)
    while y:
        x, y = x ^ y, (x & y) << 1
    return bin(x)[2:]


print(add_binary2("11", "11"))
