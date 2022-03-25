class ListNode(object):
    """
    单向链表
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def create_link_list_head(ls):
        """
        头插法，创建单向链表
        :param ls: 以 list 为基础创建链表
        :return: 返回 head
        """
        if len(ls) == 0:
            return None
        head = ListNode(ls[0])
        for i in range(1, len(ls)):
            node = ListNode(ls[i])
            node.next = head
            head = node
        return head

    @staticmethod
    def create_link_list_tail(ls):
        """
        尾插法，创建单向链表
        :param ls: 以 list 为基础创建链表
        :return: 返回 head
        """
        if len(ls) == 0:
            return None
        head = ListNode(ls[0])
        tail = head
        for i in range(1, len(ls)):
            node = ListNode(ls[i])
            tail.next = node
            tail = node
        return head

    @staticmethod
    def traverse_link_list(node):
        """
        遍历单向链表
        :param node: 开始遍历的节点
        :return: 以 list 返回所有遍历的节点
        """
        ls = list()
        while node:
            ls.append(node.val)
            node = node.next
        return ls

    @staticmethod
    def delete_node_from_link(node):
        """
        删除单向链表中的某个节点
        :param node: 要删除的节点的前驱节点
        :return: None
        """
        try:
            node.next = node.next.next
        except AttributeError:
            node.next = None
