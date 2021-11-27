""" 66. 加一
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位，数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
"""


def plus_one(digits):
    i = len(digits) - 1
    flag = 1
    while i > -1 and flag == 1:
        if digits[i] + 1 > 9:
            digits[i] = 0
            i -= 1
        else:
            digits[i] += 1
            flag = 0
    if i == -1 and flag == 1:
        temp = [1]
        temp.extend(digits)
        return temp
    else:
        return digits


ls = [9, 9]
print(plus_one(ls))
