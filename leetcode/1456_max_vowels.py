""" 1456. 定长子串中元音的最大数目
给你字符串 s 和整数 k 。

请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。

英文中的 元音字母 为（a, e, i, o, u）。

示例 1：
输入：s = "abciiidef", k = 3
输出：3
解释：子字符串 "iii" 包含 3 个元音字母。

示例 2：
输入：s = "aeiou", k = 2
输出：2
解释：任意长度为 2 的子字符串都包含 2 个元音字母。

示例 3：
输入：s = "leetcode", k = 3
输出：2
解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。

示例 4：
输入：s = "rhythms", k = 4
输出：0
解释：字符串 s 中不含任何元音字母。

示例 5：
输入：s = "tryhard", k = 4
输出：1

提示：
    1 <= s.length <= 10^5
    s 由小写英文字母组成
    1 <= k <= s.length
"""


class Solution:
    def max_vowels(self, s: str, k: int) -> int:
        vowel, res = set('aeiou'), 0  # res 最多的元音字母数量
        i = j = total = 0  # total 滑动窗口内的元音字母数量
        while j < len(s):
            if s[j] in vowel:
                total += 1
            while j == i + k - 1:
                res = max(res, total)
                if s[i] in vowel:
                    total -= 1
                i += 1
            else:
                j += 1
        return res
