from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        L = len(nums)
        if L == k:
            return

        k = k % L  # the case when k > L
        nums.reverse()

        for i in range(k // 2):
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]

        for i in range(k, (L + k) // 2):
            nums[i], nums[L - 1 - i + k] = nums[L - 1 - i + k], nums[i]

        return nums


inp_list = [1, 2, 3, 4, 5, 6, 7]
obj = Solution()
print(obj.rotate(inp_list, 3))
