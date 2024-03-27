from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = list()

        for i, val in enumerate(nums):
            import pdb

            pdb.set_trace()
            if i > 0 and nums[i - 1] == val:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    ans.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return ans


obj = Solution()
# inp1 = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
print(f"Final ans - {obj.threeSum([-1, 0, 1, 2, -1, -4])}")
# print(f"Final ans - {obj.threeSum2(inp1)}")
