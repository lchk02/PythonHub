import random

"""
LowB三人组排序算法：
1. 冒泡排序
2. 选择排序
3. 插入排序
"""


def bubble_sort0(li):
    """
    冒泡排序
    :param li: 要排序的数组
    :return: 排序后的数组
    """
    for j in range(0, len(li)-1):  # j是指要比较的趟数，有n个数，找出n-1个最大的数即可
        for i in range(0, len(li)-j-1):  # i是指向要比较的数的指针
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
            print(li)
    return li


def bubble_sort1(li):
    """
    冒泡排序
    :param li: 要排序的数组
    :return: 排序后的数组
    """
    for j in range(len(li)-1, 0, -1):  # j是指向无序区最后一个数的指针
        for i in range(0, j):  # i是指向要比较的数的指针
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
    return li


def select_sort(li):
    """
    选择排序
    :param li: 要排序的数组
    :return: 排序后的数组
    """
    n = len(li)
    for left in range(0, n-1):
        for right in range(left+1, n):
            if li[right] < li[left]:
                li[left], li[right] = li[right], li[left]
    return li


def insert_sort(li):
    for j in range(1, len(li)):
        tmp = li[j]  # j指向无序区第一个元素
        i = j - 1  # i指向有序区最后一个元素
        while tmp < li[i] and i >= 0:
            li[i+1] = li[i]
            i -= 1
        li[i+1] = tmp
    return li


li1 = [random.randint(1, 100) for i in range(5)]
print("原始数组:", li1)
# li1 = [7, 1, 2, 9, 9]
# bubble_sort1(li1)
# select_sort(li1)
print(insert_sort(li1))
