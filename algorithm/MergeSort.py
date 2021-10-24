from random import shuffle

from algorithm.CalTime import cal_time


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    tmp_li = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            tmp_li.append(li[i])
            i += 1
        else:
            tmp_li.append(li[j])
            j += 1
    while i <= mid:
        tmp_li.append(li[i])
        i += 1
    while j <= high:
        tmp_li.append(li[j])
        j += 1
    li[low:high+1] = tmp_li


def _merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        _merge_sort(li, low, mid)
        _merge_sort(li, mid+1, high)
        merge(li, low, mid, high)


@cal_time
def merge_sort(li):
    _merge_sort(li, 0, len(li)-1)
    return li
