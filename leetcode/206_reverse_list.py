""" 206. 反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

示例 2：
输入：head = [1,2]
输出：[2,1]

示例 3：
输入：head = []
输出：[]

提示：
    链表中节点的数目范围是 [0, 5000]
    -5000 <= Node.val <= 5000

进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""

from algorithm.link_list import ListNode


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        """
        迭代
        :param head:
        :return:
        """
        if head:
            tail, cur = head, head.next
            while cur:
                tail.next, cur.next = cur.next, head
                head, cur = cur, tail.next
        return head

    def reverse_list2(self, head: ListNode) -> ListNode:
        """
        递归
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        cur = self.reverse_list2(head.next)
        head.next.next, head.next = head, None
        return cur


s = Solution()
hd = ListNode.create_link_list_tail([1, 2, 3, 4, 5])
print(ListNode.traverse_link_list(s.reverse_list2(hd)))
