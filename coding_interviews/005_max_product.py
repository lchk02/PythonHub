""" 剑指 Offer II 005. 单词长度的最大乘积
给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长
度的乘积的最大值。假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。

示例 1:
输入: words = ["abcw","baz","foo","bar","fxyz","abcdef"]
输出: 16 
解释: 这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。

示例 2:
输入: words = ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4 
解释: 这两个单词为 "ab", "cd"。

示例 3:
输入: words = ["a","aa","aaa","aaaa"]
输出: 0 
解释: 不存在这样的两个单词。

提示：
    2 <= words.length <= 1000
    1 <= words[i].length <= 1000
    words[i] 仅包含小写字母
"""


def max_product(words):
    bin_word = []
    for wd in words:
        temp = 0
        for ch in wd:
            temp |= 1 << (ord(ch) - 97)
        bin_word.append(temp)
    ans, n = 0, len(words)
    for i in range(n-1):
        for j in range(i, n):
            if bin_word[i] & bin_word[j] == 0:
                ans = max(ans, len(words[i]) * len(words[j]))
    return ans
