""" 20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。

有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。

示例 1：
输入：s = "()"
输出：true

示例2：
输入：s = "()[]{}"
输出：true

示例3：
输入：s = "(]"
输出：false

示例4：
输入：s = "([)]"
输出：false

示例5：
输入：s = "{[]}"
输出：true

提示：
    1 <= s.length <= 10^4
    s 仅由括号 '()[]{}' 组成
"""


def is_valid(s):

    def couple(a, b):
        return True if (a == '(' and b == ')') or (a == '[' and b == ']') or \
                       (a == '{' and b == '}') else False

    ls = []
    for i in s:
        if len(ls) == 0:
            ls.append(i)
        else:
            if couple(ls[-1], i):
                ls.pop()
            else:
                ls.append(i)
    return len(ls) == 0
