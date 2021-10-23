""" 557. 反转字符串中的单词 III
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例：
输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"
"""


def reverse_string(s):
    for i in range(len(s)//2):
        s[i], s[-(i+1)] = s[-(i+1)], s[i]
    return s


def reverse_words(s):
    li = s.split(" ")  # ["Let's", 'take', 'LeetCode', 'contest']
    for i in range(len(li)):
        tmp = reverse_string(list(li[i]))  # ["L", "e", "t", "'", "s"]
        li[i] = ''.join(tmp)  # s'teL
    return ' '.join(li)


def reverse_words2(s):
    li = s.split(" ")
    for i in range(len(li)):
        li[i] = ''.join(reversed(list(li[i])))
    return ' '.join(li)


wds = "Let's take LeetCode contest"
print(reverse_words2(wds))
