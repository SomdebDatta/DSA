from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        i = 1
        j = len(height) - 1

        lmax = height[0]
        rmax = height[-1]

        ans = 0

        while i <= j:
            lmax = max(lmax, height[i])
            rmax = max(rmax, height[j])

            if lmax <= rmax:
                ans += lmax - height[i]
                i += 1
            else:
                ans += rmax - height[j]
                j -= 1
        return ans


ip = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
obj = Solution()
print(obj.trap(ip))
