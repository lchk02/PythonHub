from collections import defaultdict


def sum_x(arr, flag):
    n = len(arr)
    d, c, ans = defaultdict(int), defaultdict(int), [0] * n  # d用来存值上一次出现的位置，c用来存次数
    l = range(n) if flag else reversed(range(n))  # 判断正序还是逆序
    for i in l:
        j = arr[i]
        c[j] += 1  # 更新j的次数
        ans[i] = abs(i - d[j]) * (c[j] - 1) + ans[d[j]]  # 计算公式
        d[j] = i  # 更新j的位置
    return ans


def get_distances(arr):
    return list(map(lambda x, y: x + y, sum_x(arr, 1), sum_x(arr, 0)))  # 正序+逆序


# 输入：arr = [2,1,3,1,2,3,3]
# 输出：[4,2,7,2,4,4,5]
ary = [2, 1, 3, 1, 2, 3, 3]
print(get_distances(ary))
