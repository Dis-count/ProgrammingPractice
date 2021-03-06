# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

# 贪心算法

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit

# 或者 动态规划
# 定义好 每一天 持有和 未持有 两种状态即可  求解 最后一天未持有股票的状态就是最大值


#  the difference between object and no-object

class Person:
    """
    不带object
    """
    name = "zhengtong"


class Animal(object):
    """
    带有object
    """
    name = "chonghong"

if __name__ == "__main__":
    x = Person()
    print("Person", dir(x))

    y = Animal()
    print("Animal", dir(y))
