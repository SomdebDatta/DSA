from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs)
        first = sorted_strs[0]
        last = sorted_strs[-1]
        ans = ""
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans


inp = ["flower", "flow", "flight"]
inp1 = ["dog", "dracecar", "car"]
inp2 = ["a"]
inp3 = ["abcdpoi", "poitpoit", ""]
obj = Solution()
print(obj.longestCommonPrefix(inp))
print(obj.longestCommonPrefix(inp1))
print(obj.longestCommonPrefix(inp2))
print(obj.longestCommonPrefix(inp3))
