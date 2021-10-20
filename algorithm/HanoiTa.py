""" 递归
递归的两个条件：
1 调用自身；
2 递归结束条件
"""


def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    return 1


def moving(layers, a, b, c):
    if layers > 0:
        moving(layers-1, a, c, b)
        print("%s -> %s;" % (a, c))
        moving(layers-1, b, a, c)


moving(3, 'A', 'B', 'C')
