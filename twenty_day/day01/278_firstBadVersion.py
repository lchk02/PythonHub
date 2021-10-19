""" 278. 第一个错误的版本
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。
由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。
实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

示例 1：
输入：n = 5, bad = 4
输出：4
解释：
调用 isBadVersion(3) -> false 
调用 isBadVersion(5) -> true 
调用 isBadVersion(4) -> true
所以，4 是第一个错误的版本。

示例 2：
输入：n = 1, bad = 1
输出：1
"""

import random

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


def is_bad_version(version):
    # bad_version = random.randint(1, 10)
    # print("bad_version: ", bad_version)
    bad_version = 5
    print("API被调用")
    return version >= bad_version


def first_bad_version(n):
    left = 1
    right = n  # 一定存在错误的版本
    if is_bad_version(left):  # 第一个版本是错误的版本，直接返回
        return left
    else:  # 此时，第一个版本一定是正确的，最后一个版本一定是错误的
        while left < right-1:
            mid = (left + right) // 2
            flag = is_bad_version(mid)
            if flag:
                right = mid
            else:
                left = mid
        return right


def first_bad_version2(n):
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if is_bad_version(mid):
            right = mid - 1
        else:
            left = mid + 1
    else:
        return left


print(first_bad_version(5))
