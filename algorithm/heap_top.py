from random import shuffle

from algorithm.cal_time import cal_time


def sift(nums, low, high):
    """
    堆的向下调整函数，小根堆
    :param nums: 列表形式的待调整的小根堆，左右子堆为小根堆，根节点比左右节点大
    :param low: 指向根节点
    :param high: 指向最后一个叶子节点
    :return: None
    """
    i, temp = low, nums[low]  # i始终指向可被替换的节点
    j = 2 * i + 1
    while j <= high:
        if j + 1 <= high and nums[j + 1] < nums[j]:  # 大根堆反转后一个比较符
            j += 1
        if temp > nums[j]:  # 往下看一层，大根堆反转该比较符
            nums[i], i = nums[j], j
            j = 2 * i + 1
        else:  # 在中间找到了temp的位置
            nums[i] = temp
            break
    else:  # 触底
        nums[i] = temp


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
