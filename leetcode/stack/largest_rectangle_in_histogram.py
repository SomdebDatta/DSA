from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        curr_min = 0
        min_height = min(heights)
        min_area = min(heights) * len(heights)
        curr_area = 0
        curr_max_area = 0
        curr_min = 0
        max_area = min_area

        for i in range(len(heights)):
            if heights[i] == min_height:
                continue
            curr_area = curr_min = curr_max_area = heights[i]
            for j in range(i + 1, len(heights)):
                # if heights[j] == min_height:
                #     break
                # if heights[j] < curr_min:
                #     curr_min = heights[j]
                #     if curr_min * (j - i + 1) < curr_area:
                #         break
                #     else:
                #         curr_area = curr_min * (j - i + 1)
                #         continue
                # curr_area += curr_min
                curr_min = min(curr_min, heights[j])
                curr_area = curr_min * (j - i + 1)
                curr_max_area = max(curr_max_area, curr_area)
            if curr_max_area > max_area:
                print(i, heights[i], curr_max_area)
                max_area = curr_max_area
            # max_area = max(max_area, curr_area)
        return max_area


obj = Solution()
inp1 = [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]
inp2 = [2, 1, 5, 6, 2, 3]
print(obj.largestRectangleArea(inp1))
