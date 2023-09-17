from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n < 2:
            return citations[0]
        citations = sorted(citations)
        print(f"sorted citations - {citations}")
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0


inp_list = [3, 0, 6, 1, 5]
inp_list2 = [3, 2, 1, 0, 4]
inp_list3 = [9, 7, 6, 2, 1]
inp_list4 = [0, 0]
obj = Solution()
# print(obj.hIndex(inp_list))
# print(obj.hIndex(inp_list2))
print(obj.hIndex(inp_list4))
