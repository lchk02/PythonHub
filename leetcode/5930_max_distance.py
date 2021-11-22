""" 5930. 两栋颜色不同且距离最远的房子
街上有 n 栋房子整齐地排成一列，每栋房子都粉刷上了漂亮的颜色。给你一个下标从 0 开始且长度为 n
的整数数组 colors ，其中 colors[i] 表示第 i 栋房子的颜色。

返回 两栋 颜色 不同 房子之间的 最大 距离。
第 i 栋房子和第 j 栋房子之间的距离是 abs(i - j) ，其中 abs(x) 是 x 的绝对值。

示例 1：
输入：colors = [1,1,1,6,1,1,1]
输出：3
解释：上图中，颜色 1 标识成蓝色，颜色 6 标识成红色。
两栋颜色不同且距离最远的房子是房子 0 和房子 3 。
房子 0 的颜色是颜色 1 ，房子 3 的颜色是颜色 6 。两栋房子之间的距离是 abs(0 - 3) = 3 。
注意，房子 3 和房子 6 也可以产生最佳答案。

示例 2：
输入：colors = [1,8,3,8,3]
输出：4
解释：上图中，颜色 1 标识成蓝色，颜色 8 标识成黄色，颜色 3 标识成绿色。
两栋颜色不同且距离最远的房子是房子 0 和房子 4 。
房子 0 的颜色是颜色 1 ，房子 4 的颜色是颜色 3 。两栋房子之间的距离是 abs(0 - 4) = 4 。

示例 3：
输入：colors = [0,1]
输出：1
解释：两栋颜色不同且距离最远的房子是房子 0 和房子 1 。
房子 0 的颜色是颜色 0 ，房子 1 的颜色是颜色 1 。两栋房子之间的距离是 abs(0 - 1) = 1 。
"""


def max_distance(colors):
    i = 0
    j = len(colors) - 1
    while i <= j and colors[i] == colors[-1] and colors[j] == colors[0]:
        i += 1
        j -= 1
    return j


def max_distance1(colors):
    n = len(colors)
    distance = n
    flag = 0
    while flag == 0 and distance > 0:
        i = 0
        distance -= 1
        while i < n-distance and flag == 0:
            if colors[i] != colors[i+distance]:
                flag = 1
            else:
                i += 1
    return distance


cls = [1, 1]
print(max_distance(cls))
