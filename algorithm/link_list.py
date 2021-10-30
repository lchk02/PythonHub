class Node(object):
    """
    双向链表
    """
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


def create_link_list_head(ls):
    """
    头插法，创建双向链表
    :param ls: 以 list 为基础创建链表
    :return: 返回 head 和 tail
    """
    head = Node(ls[0])
    tail = head
    for i in range(1, len(ls)):
        node = Node(ls[i])
        node.next = head
        head.prev = node
        head = node
    return head, tail


def create_link_list_tail(ls):
    """
    尾插法，创建双向链表
    :param ls: 以 list 为基础创建链表
    :return: 返回 head 和 tail
    """
    head = Node(ls[0])
    tail = head
    for i in range(1, len(ls)):
        node = Node(ls[i])
        tail.next = node
        node.prev = tail
        tail = node
    return head, tail


def traverse_link_list(node, direction):
    """
    遍历链表
    :param node: 开始遍历的节点
    :param direction: 遍历的方向，1 表示向 tail 遍历，0 表示向 head 遍历
    :return: 以 list 返回所有遍历的节点
    """
    ls = list()
    if direction:
        while node:
            ls.append(node.item)
            node = node.next
    else:
        while node:
            ls.append(node.item)
            node = node.prev
    return ls


ls1 = [1, 2, 3, 4]
h, t = create_link_list_head(ls1)
print(traverse_link_list(h, 1))
