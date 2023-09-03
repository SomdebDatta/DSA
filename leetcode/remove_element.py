from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        print(index)


obj = Solution()
obj.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
obj.removeElement([3, 2, 2, 3], 3)
obj.removeElement([2], 3)
