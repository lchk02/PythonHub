"""
快排优化：每次随机取一个数，不是每次取第一个数。
"""

from algorithm.CalTime import cal_time


def partition(li, left, right):
    temp = li[left]
    while left < right:
        while li[right] >= temp and left < right:  # 先从右边找比temp小的数
            right -= 1
        li[left] = li[right]
        while li[left] <= temp and left < right:  # 从左边找比temp大的数
            left += 1
        li[right] = li[left]
    li[left] = temp
    return left


def _quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        _quick_sort(li, left, mid-1)
        _quick_sort(li, mid+1, right)


@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li) - 1)
    return li
