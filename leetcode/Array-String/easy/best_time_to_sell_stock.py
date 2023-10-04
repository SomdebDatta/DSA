"""

"""
from typing import List


class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        maxi, mini = 0, prices[0]

        for price in prices:
            if price > maxi:
                maxi = price
            if price < mini:
                mini = price

        if maxi - mini > 0:
            return maxi - mini
        else:
            return 0

    def maxProfit(self, prices: List[int]) -> int:
        profit, global_profit = 0, 0

        for buy_index in range(len(prices)):
            if buy_index == 0 or prices[buy_index] < prices[buy_index - 1]:
                for sell_index in range(len(prices) - 1, buy_index):
                    if (
                        sell_index == len(prices) - 1
                        or prices[sell_index] > prices[sell_index + 1]
                    ):
                        if prices[sell_index] - prices[buy_index] > profit:
                            profit = prices[sell_index] - prices[buy_index]
                if profit > global_profit:
                    global_profit = profit
        return profit

    def maxProfitsoln(self, prices: List[int]) -> int:
        buy_index, sell_index, max_profit, length, profit = 0, 1, 0, len(prices), 0
        import pdb

        pdb.set_trace()
        while sell_index < length:
            profit = prices[sell_index] - prices[buy_index]
            if profit > 0:
                if profit > max_profit:
                    max_profit = profit
            else:
                buy_index = sell_index
            sell_index += 1
        return max_profit


inp_list = [7, 6, 4, 3, 1]
inp_list1 = [7, 1, 5, 3, 6, 4]
inp_list2 = [2, 1, 4]
inp_list3 = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
obj = Solution()
ans = obj.maxProfitsoln(inp_list3)
print(ans)
