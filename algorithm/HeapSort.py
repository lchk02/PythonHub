from random import shuffle
from copy import deepcopy

from algorithm.CalTime import cal_time
from algorithm.QuickSort import quick_sort


def sift(li, low, high):
    """
    堆的向下调整，大根堆
    :param li: 列表形式的堆
    :param low: 指向堆顶的游标
    :param high: 指向堆底的游标
    :return: null
    """
    i = low  # 先让i指向堆顶
    j = 2 * i + 1  # j开始是指向i的左孩子
    temp = li[i]  # 将堆顶存起来
    while j <= high:
        if j+1 <= high and li[j] < li[j+1]:
            j = j + 1
        if temp < li[j]:
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
def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):  # 构建堆
        sift(li, i, n-1)
    # print(li)  # 建堆完成
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)
    return li


li0 = [i for i in range(1, 100000)]
shuffle(li0)
li1 = deepcopy(li0)
li2 = deepcopy(li0)
quick_sort(li1)
heap_sort(li2)
