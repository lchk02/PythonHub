""" 692. 前K个高频单词
给定一个单词列表words和一个整数 k ，返回前k个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。

示例 1：
输入: words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。

示例 2：
输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。

注意：
    1 <= words.length <= 500
    1 <= words[i] <= 10
    words[i]由小写英文字母组成。
    k 的取值范围是[1, 不同 words[i] 的数量]

进阶：尝试以O(n log k) 时间复杂度和O(n) 空间复杂度解决。
"""

from collections import Counter
from typing import List


class Solution:

    def compare(self, node1, node2):
        """
        比较两个节点的大小，如果 node1 大于 node2，返回 True。按字母表逐个比较，排前面的大。
        :param node1: [单词, 出现频率]
        :param node2: [单词, 出现频率]
        :return: flag: bool
        """
        flag = True
        if node1[1] > node2[1]:
            pass
        elif node1[1] == node2[1]:
            n1, n2 = len(node1[0]), len(node2[0])
            n = max(n1, n2)
            try:
                for i in range(n):
                    if ord(node1[0][i]) < ord(node2[0][i]):
                        break
                    elif ord(node1[0][i]) > ord(node2[0][i]):
                        flag = False
                        break
            except IndexError:
                flag = n1 < n2
        else:
            flag = False
        return flag

    def sift(self, nums, low, high):
        """
        堆的向下调整函数，小根堆
        :param nums: 列表形式的待调整的小根堆，左右子堆为小根堆，根节点比左右节点大
        :param low: 指向根节点
        :param high: 指向最后一个叶子节点
        :return: None
        """
        i, temp = low, [nums[low][0], nums[low][1]]  # i始终指向可被替换的节点
        j = 2 * i + 1
        while j <= high:
            if j + 1 <= high and self.compare(nums[j], nums[j + 1]):  # 大根堆反转后一个比较符
                j += 1
            if self.compare(temp, nums[j]):  # 往下看一层，大根堆反转该比较符
                nums[i][0], nums[i][1], i = nums[j][0], nums[j][1], j
                j = 2 * i + 1
            else:  # 在中间找到了temp的位置
                nums[i][0], nums[i][1] = temp[0], temp[1]
                break
        else:  # 触底
            nums[i][0], nums[i][1] = temp[0], temp[1]

    def top_k_frequent(self, words: List[str], k: int) -> List[str]:
        """
        小根堆+哈希表
        :param words:
        :param k:
        :return:
        """
        fre = Counter(words)
        ls = []
        for key, val in fre.items():
            ls.append([key, val])
        top, n = ls[:k], len(ls)
        for i in range((k-2)//2, -1, -1):
            self.sift(top, i, k-1)
        for j in range(k, n):
            if self.compare(ls[j], top[0]):
                top[0][0], top[0][1] = ls[j][0], ls[j][1]
                self.sift(top, 0, k-1)
        res = []
        for i in range(k):
            res.append(top[0][0])
            top[0][0], top[0][1] = top[k-1-i][0], top[k-1-i][1]
            self.sift(top, 0, k-1-i)
        res.reverse()
        return res

# 进阶：优先队列+哈希表
