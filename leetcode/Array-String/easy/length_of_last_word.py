class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # list_s = list(s)
        n = len(s) - 1
        space, ct = 0, 0
        while n > -1:
            if s[n] != " ":
                ct += 1
            elif ct:
                return ct
            n -= 1
        return ct


inp = "Hello World            "
inp1 = "hello"
inp2 = "a b "
inp3 = "Hello World"
obj = Solution()
print(obj.lengthOfLastWord(inp))
print(obj.lengthOfLastWord(inp1))
print(obj.lengthOfLastWord(inp2))
print(obj.lengthOfLastWord(inp3))
