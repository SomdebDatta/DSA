class Solution:
    def romanToInt(self, s: str) -> int:
        my_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        list_s, integer_ans, index = list(s), 0, 0

        while index < len(list_s):
            integer_ans += my_map[list_s[index]]
            if index > 0 and my_map[list_s[index]] > my_map[list_s[index - 1]]:
                integer_ans -= 2 * my_map[list_s[index - 1]]
            index += 1

        return integer_ans


inp = "MCM"
inp1 = "MCMXCIV"
obj = Solution()
print(obj.romanToInt(inp))
