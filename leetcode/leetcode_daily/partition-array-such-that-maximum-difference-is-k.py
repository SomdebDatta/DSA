from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        i = 0
        currMin = nums[i]
        while i < len(nums):
            if nums[i] - currMin > k:
                res += 1
                currMin = nums[i]
            i += 1
        return res + 1


obj = Solution()
nums = [3, 6, 1, 2, 5]
k = 2
print(obj.partitionArray(nums, k))
