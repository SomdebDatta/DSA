class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque

        stack = deque()
        hashmap = {"}": "{", ")": "(", "]": "["}

        if s[0] not in hashmap.values():
            return False
        stack.append(s[0])

        for i in range(1, len(s)):
            if s[i] in hashmap.values():
                stack.append(s[i])
            elif not stack or hashmap[s[i]] != stack.pop():
                return False
        if stack:
            return False
        return True


inp1 = "()"
inp2 = "()[]{}"
inp3 = "(]"
inp4 = "["
inp5 = "(){}}{"
obj = Solution()
# print(obj.isValid(inp1))
# print(obj.isValid(inp2))
# print(obj.isValid(inp3))
# print(obj.isValid(inp4))
print(obj.isValid(inp5))
