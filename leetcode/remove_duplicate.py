from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                print(i, j)
                nums[j] = nums[i]
                j += 1
        print(nums)


obj = Solution()
obj.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 10, 10, 10, 10])
