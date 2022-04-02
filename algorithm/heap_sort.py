from algorithm.cal_time import cal_time


def sift(nums, low, high):
    """
    堆的向下调整函数，大根堆
    :param nums: 列表形式的待调整的大根堆，左右子堆为大根堆，根节点比左右节点小
    :param low: 指向根节点
    :param high: 指向最后一个叶子节点
    :return: None
    """
    i, temp = low, nums[low]  # i始终指向可被替换的节点
    j = 2 * i + 1
    while j <= high:
        if j + 1 <= high and nums[j + 1] > nums[j]:  # 小根堆反转后一个比较符
            j += 1
        if temp < nums[j]:  # 往下看一层，小根堆反转该比较符
            nums[i], i = nums[j], j
            j = 2 * i + 1
        else:  # 在中间找到了temp的位置
            nums[i] = temp
            break
    else:  # 触底
        nums[i] = temp


@cal_time
def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):  # 构建堆
        sift(li, i, n-1)
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)
    return li
