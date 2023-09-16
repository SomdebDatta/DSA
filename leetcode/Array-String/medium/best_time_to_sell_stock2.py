from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] - prices[i] > 0:
                profit += prices[i + 1] - prices[i]

        return profit


inp_list = [7, 1, 5, 3, 6, 4]
inp_list2 = [1, 2, 3, 4, 5]
inp_list3 = [7, 6, 4, 3, 1]
obj = Solution()
print(obj.maxProfit(inp_list))
print(obj.maxProfit(inp_list2))
print(obj.maxProfit(inp_list3))
