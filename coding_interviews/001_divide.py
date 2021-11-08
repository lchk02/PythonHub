""" 剑指 Offer II 001. 整数除法
给定两个整数 a 和 b ，求它们的除法的商 a/b ，要求不得使用乘号 '*'、除号 '/' 以
及求余符号 '%' 。

注意：
整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及
truncate(-2.7335) = -2
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31, 2^31−1]。本题中，
如果除法结果溢出，则返回 2^31−1

示例 1：
输入：a = 15, b = 2
输出：7
解释：15/2 = truncate(7.5) = 7

示例 2：
输入：a = 7, b = -3
输出：-2
解释：7/-3 = truncate(-2.33333..) = -2

示例 3：
输入：a = 0, b = 1
输出：0

示例 4：
输入：a = 1, b = 1
输出：1
"""


def division_core(a, b):
    result = 0
    while a >= b:
        val = b
        quotient = 1
        while a >= val + val:
            quotient += quotient
            val += val
        result += quotient
        a -= val
    return result


def integer_division(a, b):
    if a == -2147483648 and b == -1:
        return 2147483647
    flag = 0
    if a < 0:
        a = -a
        flag += 1
    if b < 0:
        b = -b
        flag += 1
    result = division_core(a, b)
    return -result if flag == 1 else result


print(integer_division(-2147483648, -1))
