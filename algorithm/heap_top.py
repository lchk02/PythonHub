from random import shuffle

from algorithm.cal_time import cal_time


def sift(li, low, high):
    """
    堆的向下调整，小根堆
    :param li: 列表形式的堆
    :param low: 指向堆顶的游标
    :param high: 指向堆底的游标
    :return: null
    """
    i = low  # 先让i指向堆顶
    j = 2 * i + 1  # j开始是指向i的左孩子
    temp = li[i]  # 将堆顶存起来
    while j <= high:
        if j+1 <= high and li[j] > li[j+1]:
            j = j + 1
        if temp > li[j]:
            li[i] = li[j]
            i = j  # 往下看一层
            j = 2 * j + 1
        else:  # 中间找到了放temp的位置
            li[i] = temp
            break
    else:  # 最底层找到了放temp的位置
        li[i] = temp
    return li


@cal_time
def top_k(li, k):
    heap = li[:k]
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)
    for i in li[k+1:]:
        if i > heap[0]:
            heap[0] = i
            sift(heap, 0, k-1)
    # 挨个出数
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)
    return heap
