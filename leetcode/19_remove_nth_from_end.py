""" 19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]

提示：
    链表中结点的数目为 sz
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
"""

from algorithm.link_list import ListNode


def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = head
    slow = dummy
    count = 0
    while fast:
        fast = fast.next
        count += 1
        if count > n:
            slow = slow.next
    try:
        slow.next = slow.next.next
    except AttributeError:
        slow.next = None
    return dummy.next


ls = [1, 2, 3, 4]
hd = ListNode.create_link_list_tail(ls)
hd = remove_nth_from_end(hd, 4)
print(ListNode.traverse_link_list(hd))
