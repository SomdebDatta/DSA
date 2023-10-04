"""Moore Voting Lagorithm: 
https://leetcode.com/problems/majority-element/solutions/3676530/3-method-s-beats-100-c-java-python-beginner-friendly
/?envType=study-plan-v2&envId=top-interview-150"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = dict()
        n = len(nums) // 2
        for num in nums:
            if num in my_dict.keys():
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        for key, val in my_dict.items():
            if val > n:
                print(key)


inp_list = [2, 2, 1, 1, 1, 2, 2]
inp_list1 = [3, 2, 3]
obj = Solution()
obj.majorityElement(inp_list1)
