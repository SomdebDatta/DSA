from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ct, j = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                ct += 1
            else:
                if ct



obj = Solution()
obj.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 10, 10, 10, 10])
