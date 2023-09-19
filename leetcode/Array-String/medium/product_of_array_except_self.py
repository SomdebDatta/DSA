from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product, right_product = [1] * n, [1] * n

        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        answer = [left_product[i] * right_product[i] for i in range(n)]
        return answer


inp_list = [1, 2, 3, 4]
obj = Solution()
print(obj.productExceptSelf(inp_list))
