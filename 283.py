# 1801. Number of Orders in the Backlog
# 中等

# You are given a 2D integer array orders, where each orders[i] = [pricei, amounti, orderTypei] denotes that amounti orders have been placed of type orderTypei at the price pricei. The orderTypei is:

# 0 if it is a batch of buy orders, or
# 1 if it is a batch of sell orders.
# Note that orders[i] represents a batch of amounti independent orders with the same price and order type. All orders represented by orders[i] will be placed before all orders represented by orders[i+1] for all valid i.

# There is a backlog that consists of orders that have not been executed. The backlog is initially empty. When an order is placed, the following happens:

# If the order is a buy order, you look at the sell order with the smallest price in the backlog. If that sell order's price is smaller than or equal to the current buy order's price, they will match and be executed, and that sell order will be removed from the backlog. Else, the buy order is added to the backlog.

# Vice versa, if the order is a sell order, you look at the buy order with the largest price in the backlog. If that buy order's price is larger than or equal to the current sell order's price, they will match and be executed, and that buy order will be removed from the backlog. Else, the sell order is added to the backlog.

# Return the total amount of orders in the backlog after placing all the orders from the input. Since this number can be large, return it modulo 10^9 + 7.

#  优先队列模拟
#  优先 由  大小堆实现

from typing import List
from heapq import heappop, heappush

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        buyOrders, sellOrders = [], []
        for price, amount, order_type in orders:
            if order_type == 0:
                while amount and sellOrders and sellOrders[0][0] <= price:
                    if sellOrders[0][1] > amount:
                        sellOrders[0][1] -= amount
                        amount = 0
                        break
                    amount -= heappop(sellOrders)[1]
                    print(heappop(sellOrders))
                if amount:
                    heappush(buyOrders, [-price, amount])
            else:
                while amount and buyOrders and -buyOrders[0][0] >= price:
                    if buyOrders[0][1] > amount:
                        buyOrders[0][1] -= amount
                        amount = 0
                        break
                    amount -= heappop(buyOrders)[1]
                if amount:
                    heappush(sellOrders, [price, amount])
        return (sum(x for _, x in buyOrders) + sum(x for _, x in sellOrders)) % MOD


test = Solution()

orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]

res = test.getNumberOfBacklogOrders(orders)

