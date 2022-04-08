""" 144. 二叉树的前序遍历
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

示例 1：
输入：root = [1,null,2,3]
输出：[1,2,3]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]

示例 5：
输入：root = [1,null,2]
输出：[1,2]

提示：
    树中节点数目在范围 [0, 100] 内
    -100 <= Node.val <= 100

进阶：递归算法很简单，你可以通过迭代算法完成吗？
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, res, cur = [], [], root
        while cur or stack:
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.left
            cur = stack.pop().right
        return res

    def perorder_traversal2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, res = [root], []
        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return res
