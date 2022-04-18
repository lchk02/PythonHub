"""
一天一只顽猴想要从山脚爬到山顶
途中经过一个有n个台阶的阶梯，但是这个猴子有个习惯，每一次只跳1步或3步
试问？猴子通过这个阶梯有多少种不同的跳跃方式

输入描述：
输入只有一个这个数n    0<n<50
此阶梯有多个台阶
输出描述：
有多少种跳跃方式

示例1:
输入
 50
输出
  122106097

示例2:
输入
  3
输出
  2
"""


class Solution:
    def climb_stair(self, n: int) -> int:
        dp = [[0, 0] for _ in range(n)]
        dp[0], dp[1], dp[2] = [1, 0], [1, 0], [1, 1]
        for i in range(3, n):
            dp[i][0] = sum(dp[i-1])
            dp[i][1] = sum(dp[i-3])
        return sum(dp[n-1])


sl = Solution()
print(sl.climb_stair(50))
