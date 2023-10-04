from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n - 1):
            print("he")
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        print(candies)
        for i in range(n - 2, 0, -1):
            print(i)
            if ratings[i] > ratings[i + 1] and (candies[i] <= candies[i + 1]):
                candies[i] = candies[i + 1] + 1
        print(candies)
        if len(ratings) > 1:
            if ratings[0] > ratings[1]:
                candies[0] = candies[1] + 1
            if ratings[-1] > ratings[-2]:
                candies[-1] = candies[-2] + 1
        return sum(candies)


inp_list = [7, 1, 5, 3, 6, 4]
inp_list2 = [1, 2, 3, 4, 5]
inp_list3 = [7, 6, 4, 3, 1]
sample_ip1 = [1, 0, 2]
sample_ip2 = [1, 2, 2]
sample_ip_3 = [1, 3, 2, 2, 1]
sample_ip_4 = [1, 2, 87, 87, 87, 2, 1]
obj = Solution()
# print(obj.candy(inp_list))
# print(obj.candy(inp_list2))
# print(obj.candy(inp_list3))
# print(obj.candy(sample_ip1))
# print(obj.candy(sample_ip2))
print(obj.candy(sample_ip_4))
