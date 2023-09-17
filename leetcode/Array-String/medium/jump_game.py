from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable_index = 0
        for i in range(len(nums)):
            if i + nums[i] > max_reachable_index:
                max_reachable_index = i + nums[i]
            if i == max_reachable_index:
                break
        return max_reachable_index >= len(nums) - 1


inp_list = [2, 3, 1, 1, 4]
inp_list2 = [3, 2, 1, 0, 4]
obj = Solution()
print(obj.canJump(inp_list))
print(obj.canJump(inp_list2))
