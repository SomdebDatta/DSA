class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for position, letter in enumerate(haystack):
            if letter == needle[0]:
                if haystack[position : position + len(needle)] == needle:
                    return position
        return -1


obj = Solution()
print(obj.strStr("sadbutsad", "sad"))
print(obj.strStr("leetcodel", "leeto"))
# print(obj.strStr(inp1))
# print(obj.strStr(inp2))
# print(obj.strStr(inp3))
